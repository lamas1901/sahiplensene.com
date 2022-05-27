from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from slugify import slugify


import re
import urllib

from .models import Pet, Slide


def about_us(request):
	return render(request,'pets/about_us.html')

def contact_us(request):
	return render(request,'pets/contact_us.html')

def home(request):

	slides = Slide.objects.all()

	super_pets = Pet.objects.all().filter(advert_type='super')
	platinum_pets = Pet.objects.all().filter(advert_type='platinum')
	gold_pets = Pet.objects.all().filter(advert_type='gold')
	silver_pets = Pet.objects.all().filter(advert_type='silver')

	return render(request,'pets/home.html',{
		'slides':slides,
		'super_pets':super_pets,
		'platinum_pets':platinum_pets,
		'gold_pets':gold_pets,
		'silver_pets':silver_pets
	})


def dashboard(request):

	pets = Pet.objects.all()

	straight_filters = [
		'city',
		'sex',
		'type'
	]
	range_filters = [
		'price',
		'height',
		'age'
	]

	# переменная для передачи в шаблон для сохранение состояний переключателей фильтров
	filter_values = {}

	# применить фильтр сортировки
	if request.GET.get('keyword'):
		pets = pets.filter(name__icontains=request.GET['keyword'])
		filter_values['keyword'] = request.GET['keyword']

	# перебор простых фильтров
	for filter_name in straight_filters:
		if request.GET.get(filter_name) and request.GET.get(filter_name) != 'all':
			_ = request.GET[filter_name]
			pets = pets.filter(**{'animal_type' if filter_name == 'type' else filter_name:_})
			filter_values[filter_name] = _

	# перебор диапозоновых фильтров
	for filter_name in range_filters:		
		if request.GET.get(filter_name):
			_ = re.findall(r'(\d+|Bedava)',request.GET[filter_name])
			ismax = '+' in request.GET[filter_name]
			
			if len(_)==2:
				_[0] = _[0] if _[0].isnumeric() else 0
				pets = pets.filter(
					**{
						f'{filter_name}__gte':_[0],
						f'{filter_name}__lte':_[1] if not ismax else 999999
					}
				)
			
			filter_values[filter_name] = _

	# применить фильтр сортировки
	if request.GET.get('sort') and getattr(Pet,request.GET.get('sort').replace('-',''),False):
		pets = pets.order_by(f'{request.GET.get("sort")}')
		filter_values['sort'] = request.GET.get('sort')

	# строка запроса get для сохранения фильтров при использовании пагинации
	filter_string = ""
	for _ in straight_filters+range_filters:
		if request.GET.get(_):
			filter_string += f'{_}={urllib.parse.quote(request.GET.get(_))}&'

	paginator = Paginator(pets,9)
	page = request.GET.get('page')

	try:
		pets = paginator.page(page)
	except PageNotAnInteger:
		pets = paginator.page(1)
	except EmptyPage:
		pets = paginator.page(paginator.num_pages)


	return render(request,'pets/dashboard.html',{'pets':pets,'filter_string':filter_string,'filter_values':filter_values})


class PetDetailView(DetailView):
	model = Pet
	template_name = 'pets/pet.html'

	def get_object(self,queryset=None):
		return Pet.objects.get(id=self.kwargs.get('pk'),slug=self.kwargs.get('slug'))


class PetAddView(CreateView,LoginRequiredMixin):
	model = Pet
	fields = ['name','animal_type','breed','color','age','height','price','city','sex','photo']
	template_name = 'pets/pet-add.html'

	def get_form(self, form_class=None):
		form = self.get_form_class()(**self.get_form_kwargs())
		form.fields['photo'].widget.attrs.update({'onchange':'preview();'})
		for field in form.fields:
			form.fields[field].widget.attrs.update({'class':'form-control'})

		return form

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.slug = slugify(instance.name)
		instance.owner = self.request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())


class PetEditView(UpdateView,LoginRequiredMixin):
	model = Pet
	fields = ['name','animal_type','breed','color','age','height','price','city','sex','photo']
	template_name = 'pets/pet-add.html'

	def get_form(self, form_class=None):

		form = self.get_form_class()(**self.get_form_kwargs())
		form.fields['photo'].widget.attrs.update({'onchange':'preview();'})
		for field in form.fields:
			form.fields[field].widget.attrs.update({'class':'form-control'})

		return form

@login_required(login_url='profiles:custom-login')
def pet_delete(request,id):
	pet = get_object_or_404(Pet,id=id)
	if pet.owner.id == request.user.id:
		pet.delete()
	return redirect(to='pets:my-pets')

@login_required(login_url='profiles:custom-login')
def my_pets(request):
	mypets = Pet.objects.all().filter(owner=request.user)
	return render(request,'pets/my-pets.html',{'mypets':mypets})




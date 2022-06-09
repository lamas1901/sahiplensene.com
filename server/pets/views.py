from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from slugify import slugify


import re
import urllib

from .models import Pet, PetType, Slide, VideoSlide, FrequentlyAskedQuestion
from .utils import consts


def about_us(request):
	return render(request,'pets/about_us.html')

def contact_us(request):
	return render(request,'pets/contact_us.html')

def home(request):

	slides = Slide.objects.all()
	video_slides = VideoSlide.objects.all()

	super_pets = Pet.objects.all().filter(advert_type='super')
	platinum_pets = Pet.objects.all().filter(advert_type='platinum')
	silver_pets = Pet.objects.all().filter(advert_type='silver')

	gold_pets_dogs = Pet.objects.filter(animal_type=PetType.objects.get(slug='kopek'),advert_type='gold')
	gold_pets_cats = Pet.objects.filter(animal_type=PetType.objects.get(slug='kedi'),advert_type='gold')
	gold_pets_birds = Pet.objects.filter(animal_type=PetType.objects.get(slug='kus'),advert_type='gold')


	return render(request,'pets/home.html',{
		'slides':slides,
		'video_slides': video_slides,
		'gold_pets_dogs':gold_pets_dogs,
		'gold_pets_cats':gold_pets_dogs,
		'gold_pets_birds':gold_pets_birds
	})


def dashboard(request,type='normal'):

	type = type if type in [x[0] for x in consts.ADVERT_CHOICES] else type

	pets = Pet.objects.filter(advert_type=type).order_by('publish')

	straight_filters = [
		'city',
		'sex',
		'animal_type'
	]
	range_filters = [
		'price',
		'height',
		'age'
	]

	# переменная для передачи в шаблон для сохранение состояний переключателей фильтров
	filter_values = {}

	# sorting
	if request.GET.get('keyword'):
		pets = pets.filter(name__contains=request.GET['keyword'])
		filter_values['keyword'] = request.GET['keyword']

	# straight filters
	for filter_name in straight_filters:
		if request.GET.get(filter_name):
			filter_value = request.GET[filter_name]
			if filter_name=='animal_type':
				pets = pets.filter(animal_type=PetType.objects.get(slug=filter_value)) if filter_value else pets
			else:
				pets = pets.filter(**{filter_name:filter_value}) if filter_value else pets
			filter_values[filter_name] = filter_value

	# range filters
	for filter_name in range_filters:		
		if request.GET.get(filter_name):
			filter_range = re.findall(r'(\d+|Bedava)',request.GET[filter_name])
			ismax = '+' in request.GET[filter_name]
			
			if len(filter_range)==2:
				filter_range[0] = filter_range[0] if filter_range[0].isnumeric() else '0'
				if int(filter_range[0]) and (not ismax):
					pets = pets.filter(
						**{
							f'{filter_name}__gte':int(filter_range[0]),
							f'{filter_name}__lte':int(filter_range[1]) if not ismax else 999999
						}
					)
			
			filter_values[filter_name] = filter_range

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


	return render(request,'pets/dashboard.html',{
			'pets': pets,
			'type': type,
			'filter_string':filter_string,
			'filter_values':filter_values
		}
	)


class PetDetailView(DetailView):
	model = Pet
	template_name = 'pets/pet.html'

	def get_object(self,queryset=None):
		return Pet.objects.get(id=self.kwargs.get('pk'),slug=self.kwargs.get('slug'))


class PetAddView(LoginRequiredMixin,CreateView):
	model = Pet
	login_url = '/profiles/login'
	fields = ['name','animal_type','breed','color','age','height','price','city','sex','photo','description']
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


class PetEditView(LoginRequiredMixin,UpdateView):
	model = Pet
	login_url = '/profiles/login'
	fields = ['name','animal_type','breed','color','age','height','price','city','sex','photo','description']
	template_name = 'pets/pet-add.html'

	def get_form(self, form_class=None):

		form = self.get_form_class()(**self.get_form_kwargs())
		form.fields['photo'].widget.attrs.update({'onchange':'preview();'})
		for field in form.fields:
			form.fields[field].widget.attrs.update({'class':'form-control'})

		return form

	def get(self, request, *args, **kwargs):
		if request.user == self.get_object().owner:
			return super().get(request, *args, **kwargs)
		return HttpResponseRedirect("/")

class FAQListView(ListView):
	template_name = 'pets/faq.html'
	paginate_by = 10
	model = FrequentlyAskedQuestion


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




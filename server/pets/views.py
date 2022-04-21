from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from django.shortcuts import render, get_object_or_404, redirect
from slugify import slugify

import re
import urllib

from .forms import PetForm
from .models import Pet, Slide


def home(request):
	slides = Slide.objects.all()

	super_pets 		= Pet.objects.all().filter(advert_type='super')
	platinum_pets 	= Pet.objects.all().filter(advert_type='platinum')
	gold_pets 		= Pet.objects.all().filter(advert_type='gold')
	silver_pets 	= Pet.objects.all().filter(advert_type='silver')

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


def pet_details(request,slug,id):
	pet = get_object_or_404(
		Pet,
		slug=slug,
		id=id
	) 
	return render(request,'pets/pet_details.html',{'pet':pet})


@login_required(login_url='profiles:custom-login')
def pet_add(request):
	if request.method == 'POST':
		form = PetForm(request.POST,request.FILES)
		print(request.FILES)
		if form.is_valid():
			if len(Pet.objects.all().filter(owner=request.user)) < 10:
				pet = Pet(
					slug = 			slugify(form.cleaned_data['name']),
					name = 			form.cleaned_data['name'],
					animal_type = 	form.cleaned_data['animal_type'],
					breed = 		form.cleaned_data['breed'],
					color = 		form.cleaned_data['color'],
					age = 			form.cleaned_data['age'],
					height = 		form.cleaned_data['height'],
					price = 		form.cleaned_data['price'],
					city = 			form.cleaned_data['city'],
					sex = 			form.cleaned_data['sex'],
					photo = 		form.cleaned_data['photo'],
					description = 	form.cleaned_data['description'],
					owner = 		request.user
				)
				pet.save()
				messages.success(request,message='İlanınız yayınlandı!')
				form = PetForm()
			else:
				messages.error(request,message='10 ilandan fazla ilan veremezsiniz! İlan vermek için mevcut ilanınızı silin...')
	else:
		form = PetForm()
	return render(request,'pets/pet_add.html',{'form':form})


@login_required(login_url='profiles:custom-login')
def pet_edit(request,id):
	pet = Pet.objects.all().get(id=id)
	if request.method == 'POST':
		form = PetForm(request.POST,request.FILES,instance=pet)
		if form.is_valid():
			form.save()
			messages.success(request,'Değişiklikler kaydedildi')
	else:
		form = PetForm(instance=pet)

	return render(request,'pets/pet_add.html',{'form':form,'pet':pet})


@login_required(login_url='profiles:custom-login')
def mypets(request):
	mypets = Pet.objects.all().filter(owner=request.user)
	return render(request,'pets/mypets.html',{'mypets':mypets})


@login_required(login_url='profiles:custom-login')
def mypets_delete(request,id):
	pet = get_object_or_404(Pet,id=id)
	if pet.owner.id == request.user.id:
		pet.delete()
	return redirect(to='pets:mypets')


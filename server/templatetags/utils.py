from django import template
from django.utils.safestring import mark_safe
import markdown

from pets.models import PetType, Pet, Media, FrequentlyAskedQuestion
from pets.utils.consts import (
	CITIES, 
	ADVERT_CHOICES, 
	ADVERT_COLORS
)
from pets.utils import consts
from blog.models import Post 

register = template.Library()

@register.filter
def is_undefined(text):
	return text if text else 'Belirtilmedi'

@register.filter(name='markdown')
def makrdown_format(text):
	return mark_safe(markdown.markdown(text))

@register.simple_tag
def define(val=None):
  return val

# ADVERT_HIERARCHY 

@register.simple_tag
def get_advert_type(slug):
	for level in ADVERT_CHOICES:
		if level[0] == slug:
			return level[1]

@register.simple_tag
def get_advert_type_color(slug):
	return ADVERT_COLORS.get(slug,'')

@register.inclusion_tag('pets/component/pet-type-badge.html')
def pet_type_badge(slug):
	return {'slug':slug}

# PET TYPE

@register.simple_tag
def get_pet_types():
	pet_types = PetType.objects.all()
	if pet_types:
		return PetType.objects.all()
	else:
		return []

@register.simple_tag
def get_pet_type(slug):
	pet_type = PetType.objects.filter(slug=slug)
	if pet_type:
		return PetType.objects.get(slug=slug).name
	else:
		return None

@register.simple_tag
def get_pets_by_type(type,exclude=0,count=5):
	return Pet.objects.all().exclude(id=exclude).filter(animal_type=type)[:count]

# PET CITIES

@register.simple_tag
def get_cities():
	return consts.CITIES
	
@register.simple_tag
def get_city(slug):
	for city in CITIES:
		if city[0] == slug:
			return city[1]

# POSTS

@register.simple_tag
def get_recent_posts(count=5):
	return Post.objects.all().order_by('-publish')[:count]

@register.simple_tag
def get_posts_for_pet_type(type,count=5):
	return Post.objects.all().filter(for_pet_type=type)[:count]

@register.inclusion_tag('_origin/component/pagination.html')
def pagination(objects,get_params_string=''):
	return {
		'objects':objects,
		'get_params_string':get_params_string
	}


# PET

@register.simple_tag
def get_mypet_count(request):
	return len(Pet.objects.filter(owner=request.user))

# SHOP_DATA

@register.simple_tag
def get_global_const(name):
	return consts.SHOP_DATA[name]

@register.simple_tag
def get_const(name):
	return getattr(consts,name)

@register.simple_tag
def get_media():
	return Media.objects.all()

# GET FEW MODEL OBJECTS

@register.simple_tag
def get_faq(count=5):
	return FrequentlyAskedQuestion.objects.all()[:count]
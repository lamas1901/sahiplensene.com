from django import forms

from .utils import consts
from .models import PetType,Pet

try:
	ANIMAL_CHOICES = tuple((pet_type.slug,pet_type.name) for pet_type in PetType.objects.all())
except:
	ANIMAL_CHOICES = consts.DEFAULT_ANIMAL_TYPES

class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = [
			'breed',
			'color',
			'name',
			'age',
			'height',
			'price',
			'description',
			'photo',
			'sex',
			'animal_type',
			'city'
		]
		default_attrs = {'class':'form-control'}
		widgets = {
			'breed':	forms.TextInput(attrs=default_attrs),
			'color':	forms.TextInput(attrs=default_attrs),
			'name':		forms.TextInput(attrs=default_attrs),
			'age':		forms.NumberInput(attrs=default_attrs),
			'height': 	forms.NumberInput(attrs=default_attrs),
			'price': 	forms.NumberInput(attrs=default_attrs),
			'animal_type':forms.Select(attrs=default_attrs),
			'sex': 		forms.Select(attrs=default_attrs),
			'city':		forms.Select(attrs=default_attrs),
			'photo':	forms.FileInput(attrs=default_attrs|{'onchange':'preview();'}),
			'description': forms.Textarea(attrs=default_attrs|{'rows':10})
		}



from django import forms

from .utils import consts
from .models import PetType,Pet

try:
	ANIMAL_CHOICES = tuple((pet_type.slug,pet_type.name) for pet_type in PetType.objects.all())
except:
	ANIMAL_CHOICES = consts.DEFAULT_ANIMAL_TYPES

class PetForm(forms.ModelForm):

	# name = 			forms.CharField(max_length=255,required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
	# price = 		forms.IntegerField(required=True,widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
	# age = 			forms.IntegerField(required=True,widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
	# height = 		forms.IntegerField(required=True,widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
	# breed = 		forms.CharField(max_length=255,required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
	# color = 		forms.CharField(max_length=50,required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
	# description = 	forms.CharField(required=True,widget=forms.widgets.Textarea(attrs={'class':'form-control','rows':10}))
	# photo = 		forms.ImageField(required=True,widget=forms.widgets.FileInput(attrs={'class':'form-control','onchange':'preview()','id':'formFile'}))



	# sex = forms.ChoiceField(required=True,widget=forms.widgets.Select(attrs={'class':'form-select'}),
	# 	choices=(
	# 		('male','Erkek'),
	# 		('female','Dişi')
	# 	),
	# )
	# animal_type = forms.ChoiceField(required=True,widget=forms.widgets.Select(attrs={'class':'form-select'}),
	# 	choices=ANIMAL_CHOICES
	# )
	# city = forms.ChoiceField(required=True,widget=forms.widgets.Select(attrs={'class':'form-select'}),
	# 	choices=consts.CITIES
	# )
	pass
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



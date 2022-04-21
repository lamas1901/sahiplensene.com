from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .utils import consts

class PetType(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,unique=True)

class Pet(models.Model):
	CITY_CHOICES = consts.CITIES
	SEX_CHOICES = (
		('male','Erkek'),
		('female','Dişi')
	)

	try:
		ANIMAL_CHOICES = tuple((pet_type.slug,pet_type.name) for pet_type in PetType.objects.all())
	except:
		ANIMAL_CHOICES = consts.DEFAULT_ANIMAL_TYPES

	ADVERT_CHOICES = consts.ADVERT_HIERARCHY

	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,unique_for_date='publish')
	publish = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	advert_type = models.CharField(max_length=50,choices=ADVERT_CHOICES,default=ADVERT_CHOICES[0][0])
	price = models.IntegerField()
	animal_type = models.CharField(max_length=50,choices=ANIMAL_CHOICES,default=ANIMAL_CHOICES[0][0])
	age = models.IntegerField()
	color = models.CharField(max_length=50)
	height = models.IntegerField()
	sex = models.CharField(max_length=50,choices=SEX_CHOICES,default='male')
	breed = models.CharField(max_length=255)
	city = models.CharField(max_length=50,choices=CITY_CHOICES,default=CITY_CHOICES[0][0])
	photo = models.ImageField(upload_to='pets/photos')
	description = models.TextField()

	def get_absolute_url(self):
		return reverse('pets:pet', args=[
			self.slug,
			self.id
		])

class Slide(models.Model):

	heading_pre = models.CharField(max_length=50)
	heading = models.CharField(max_length=50)
	heading_sub = models.CharField(max_length=100)

	button_show = models.BooleanField(default=False)
	button_text = models.CharField(max_length=50)
	button_link = models.TextField()

	image = models.ImageField(upload_to='pets/slider')

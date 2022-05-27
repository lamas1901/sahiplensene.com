from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .utils import consts

class PetType(models.Model):
	name = models.CharField('Tür Adı',max_length=255)
	slug = models.SlugField('Slug',max_length=255,unique=True)

	def __str__(self):
		return self.name

	def __repr__(self):
		return f'<PetType-{self.name}>'

class Pet(models.Model):

	name = models.CharField('Hayvan Adı',max_length=255)
	slug = models.SlugField('Slug',max_length=255,unique_for_date='publish')
	publish = models.DateTimeField('Yayınlama Tarihi',default=timezone.now)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	advert_type = models.CharField('İlan Türü',max_length=50,choices=consts.ADVERT_CHOICES,default=consts.ADVERT_CHOICES[0][0])
	price = models.IntegerField('İlan Fiyatı (Bedava ise 0)')
	animal_type = models.ForeignKey(PetType,on_delete=models.CASCADE)
	age = models.IntegerField('Hayvan Yaşı')
	color = models.CharField('Hayvan Rengi',max_length=50)
	height = models.IntegerField('Hayvan Boyu',)
	sex = models.CharField('Hayvan Cinsi',max_length=50,choices=consts.SEX_CHOICES,default='male')
	breed = models.CharField('Hayvan Irkı',max_length=255)
	city = models.CharField('Bulunduğu Şehir',max_length=50,choices=consts.CITIES,default=consts.CITIES[0][0])
	photo = models.ImageField('Görüntü',upload_to='pets/photos')
	description = models.TextField('Açıklama')

	def get_absolute_url(self):
		return reverse('pets:pet', args=[
			self.slug,
			self.id
		])

	def __str__(self):
		return self.name

	def __repr__(self):
		return f'<Pet-{self.name}>'


class Slide(models.Model):

	heading_pre = models.CharField('Üst Başlık',max_length=50)
	heading = models.CharField('Başlık',max_length=50)
	heading_sub = models.CharField('',max_length=100)

	button_show = models.BooleanField('Tuş Ekle',default=False)
	button_text = models.CharField('Tuş Yazısı',max_length=50)
	button_link = models.TextField('Tuş Linki')

	image = models.ImageField('Arka Plan',upload_to='pets/slider')

	def __repr__(self):
		return f'<Slide-{self.heading}>'


class Media(models.Model):
	name = models.CharField('Medya Adı',max_length=50)
	link = models.TextField('Medya Linki')
	fa_icon = models.CharField('Medya İkonu',max_length=50)

	def __str__(self):
		return self.name

	def __repr__(self):
		return f'<Media-{self.name}>'
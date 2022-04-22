from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

from pets.utils import consts
from pets.models import PetType

class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published')
	)
	
	try:
		ANIMAL_CHOICES = tuple((pet_type.slug,pet_type.name) for pet_type in PetType.objects.all())
	except:
		ANIMAL_CHOICES = ()

	if not len(ANIMAL_CHOICES):
		ANIMAL_CHOICES = consts.DEFAULT_ANIMAL_TYPES
		
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50,unique_for_date='publish')
	image = models.ImageField(upload_to='blog/posts')
	excerpt = models.CharField(max_length=255)
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	for_pet_type = models.CharField(max_length=20,choices=ANIMAL_CHOICES,default=ANIMAL_CHOICES[0][0])
	tags = TaggableManager()

	def get_absolute_url(self):
		return reverse('blog:post_details',
			args= [self.slug]
		)
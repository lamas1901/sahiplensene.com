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
	
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50,unique_for_date='publish')
	image = models.ImageField(upload_to='blog/posts')
	excerpt = models.CharField(max_length=255)
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	for_pet_type = models.ForeignKey(PetType,on_delete=models.CASCADE)
	tags = TaggableManager()

	def get_absolute_url(self):
		return reverse('blog:post_details',
			args= [ self.slug ]
		)
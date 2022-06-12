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
	
	title = models.CharField('Başlık',max_length=255)
	slug = models.SlugField('Slug',max_length=255,unique_for_date='publish')
	# image = models.ImageField('Resim',upload_to='blog/posts',blank=True,null=True)
	excerpt = models.CharField('Alt Başlık',max_length=255)
	content = models.TextField('İçerik')
	publish = models.DateTimeField('Yayınlama Tarihi',default=timezone.now)
	status = models.CharField('Statüs',max_length=10,choices=STATUS_CHOICES,default='draft')
	for_pet_type = models.ForeignKey(PetType,on_delete=models.CASCADE)
	tags = TaggableManager()

	# def save(self, *args, **kwargs):
	# 	from PIL import Image
	# 	super().save()
	# 	img = Image.open(self.image.path)
	# 	if img.height > 100 or img.width > 100:
	# 		new_img = (100, 100)
	# 		img.thumbnail(new_img)
	# 		img.save(self.image.path)


	def get_absolute_url(self):
		return reverse('blog:post_details',
			args= [ self.slug ]
		)

	def __repr__(self):
		return f'<Post-"{self.title}">'

	def __str__(self):
		return f'"{self.title}" adlı Yazı'
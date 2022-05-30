from django.contrib import admin

from .models import Pet, PetType, Slide, VideoSlide, Media

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	date_hierarchy = 'publish'
	list_display = ('name','owner','publish','animal_type')
	list_filter = ('name','publish','price','age','city')
	ordering = ('publish',)
	prepopulated_fields = {'slug':('name',)}
	raw_id_fields = ('owner',)
	search_fields = ('name','description')

@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	ordering = ('name','slug')
	prepopulated_fields = {'slug':('name',)}
	search_fields = ('name','slug')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
	list_display = ('id',)
	ordering = ('id',)

@admin.register(VideoSlide)
class VideoSlideAdmin(admin.ModelAdmin):
	list_display = ('id',)
	ordering = ('id',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
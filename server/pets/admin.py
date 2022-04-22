from django.contrib import admin

from .models import Pet, PetType, Slide, Media

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
	list_display = ('heading',)
	ordering = ('heading',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
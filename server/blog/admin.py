from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'publish'
	list_display = ('title','status','publish','for_pet_type')
	list_filter = ('status','publish')
	ordering = ('status','publish')
	prepopulated_fields = {'slug':('title',)}
	search_fields = ('title','content')

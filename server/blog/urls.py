from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('',views.blog,name='posts'),
	path('<str:slug>',views.post_details,name='post_details')
]
from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
	path('',views.home,name='home'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('dashboard/<str:type>/',views.dashboard,name='dashboard'),
	path('pet/<slug:slug>/<int:pk>',views.PetDetailView.as_view(),name='pet'),
	path('pet_add/',views.PetAddView.as_view(),name='pet-add'),
	path('pet_edit/<slug:pk>',views.PetEditView.as_view(),name='pet-edit'),
	path('pet_delete/<int:id>',views.pet_delete,name='pet-delete'),
	path('my_pets/',views.my_pets,name='my-pets'),
	path('about_us/',views.about_us,name='about-us'),
	path('contact_us',views.about_us,name='contact-us')
]
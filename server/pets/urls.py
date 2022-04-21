from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
	path('',views.home,name='home'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('pet/<slug:slug>/<int:id>',views.pet_details,name='pet'),
	path('add_pet/',views.pet_add,name='add_pet'),
	path('edit_pet/<int:id>',views.pet_edit,name='edit_pet'),
	path('mypets/',views.mypets,name='mypets'),
	path('mypets_delete/<int:id>',views.mypets_delete,name='mypets-delete')
]
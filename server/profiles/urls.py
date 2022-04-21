from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'profiles'

urlpatterns = [
	path('',views.profile,name='profile'),
	path('password',views.profile_password,name='profile-password'),
	path('logout',views.logout_view,name='logout'),
	path('login',views.CustomLoginView.as_view(
		redirect_authenticated_user=True,
		template_name='profiles/login.html',
		authentication_form=LoginForm
	),name='custom-login'),
	path('register',views.RegisterView.as_view(),name='register'),
	path('verify',views.verify,name='verify'),
	path('verify/<str:email>/<str:code>',views.register),
	path('password-forgot',views.password_forgot,name='password-forgot'),
	path('password-change',views.password_change,name='password-change')
]
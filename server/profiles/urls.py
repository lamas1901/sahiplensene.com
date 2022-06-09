from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

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
	path('verify',views.verify,name='verify'),
	path('verify/<str:email>/<str:code>',views.register,name='verify-confirm'),
	path('password-reset',views.ResetPasswordView.as_view(),name='password-reset'),
	path('password-change/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='profiles/password-change.html',success_url=reverse_lazy('profiles:custom-login')),name='password-change')
]
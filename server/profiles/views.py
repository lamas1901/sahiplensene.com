from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views import View
from django.urls import reverse, reverse_lazy

import secrets

from . import forms
from .forms import RegisterForm, LoginForm, UserForm, ProfileForm, VerifyForm
from .models import SignUpRequest

@login_required(login_url='profiles:custom-login')
def profile(request):

	if request.method == 'POST':
		form_user = UserForm(request.POST,instance=request.user)
		form_profile = ProfileForm(request.POST,instance=request.user.profile)

		if form_user.is_valid() and form_profile.is_valid():
			form_user.save()
			form_profile.save()
			messages.success(request,'Profil bilgileriniz başarı ile güncellendi')
			return redirect(to='/profile')

	else:
		form_user = UserForm(instance=request.user)
		form_profile = ProfileForm(instance=request.user.profile)

	return render(request,'profiles/profile.html',{
		'form_user':form_user,
		'form_profile':form_profile,
	})


@login_required(login_url='profiles:custom-login')
def profile_password(request):

	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Parolanız başarı ile değiştirildi!')
			return redirect('profiles:profile-password')
		else:
			messages.error(request, 'Lütfen istenen bilgileri doğru giriniz')
	else:
		form = PasswordChangeForm(request.user)

	return render(request,'profiles/profile-password.html',{'form':form})

class CustomLoginView(LoginView):
	form_class = LoginForm

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect(reverse('pets:home'))
		return super().dispatch(*args, **kwargs)

	def form_valid(self,form):
		remember_me = form.cleaned_data.get('remember_me')

		if not remember_me:
			self.request.session.set_expiry(0)
			self.request.session.modified = True 

		return super(CustomLoginView,self).form_valid(form)


def verify(request):

	if request.user.is_authenticated:
		return redirect('pets:home')

	if request.method == 'POST':

		form = VerifyForm(request.POST)

		if form.is_valid():

			if not User.objects.filter(email=form.cleaned_data['email']):

				while True:
					code = secrets.token_urlsafe()
					if SignUpRequest.objects.filter(code=code):
						continue
					break

				if SignUpRequest.objects.filter(email=form.cleaned_data['email']):
					SignUpRequest.objects.get(email=form.cleaned_data['email']).delete()

				sign_up_request = SignUpRequest(email=form.cleaned_data['email'],code=code)
				sign_up_request.save()

				mail = EmailMessage(
					'Sahiplensene E-posta doğrulama.',
					render_to_string('profiles/mail/verify.html',{
						'link':f'{request.scheme}://{request.get_host()}{reverse("profiles:verify-confirm",args=[form.cleaned_data["email"],code])}'
					}),
					settings.DEFAULT_FROM_EMAIL,
					[form.cleaned_data['email']],
				)
				mail.content_subtype = 'html'
				mail.send()
				messages.success(request,f'E-postanıza ({form.cleaned_data["email"]}) doğrulama linki gönderildi. Kontrol edip geçiş yapınız...')
				form = VerifyForm()

			else:
				
				messages.error(request,'Bu e-posta ile kayıtlı üye şuan mevcut. Kontrol ediniz...')
	else:
		form = VerifyForm()

	return render(request,'profiles/verify.html',{'form':form})


def register(request,email,code):
	if SignUpRequest.objects.filter(email=email,code=code):
		sign_up_request = SignUpRequest.objects.get(email=email,code=code)
		if request.method == 'POST':
			form_user = RegisterForm(request.POST)
			form_profile = ProfileForm(request.POST)
			if form_user.is_valid() and form_profile.is_valid():
				user = form_user.save(commit=False)
				profile = form_profile.save(commit=False)
				user.email = email
				profile.user = user
				user.save()
				profile.save()
				sign_up_request.delete()
				messages.success(request,'Hesabınız oluşturuldu')
				form_user = RegisterForm()
				form_profile = ProfileForm()
				return redirect('profiles:custom-login')
		else:
			form_user = RegisterForm()
			form_profile = ProfileForm()
		return render(request,'profiles/register.html',{'form_user':form_user,'form_profile':form_profile})
	return redirect('pets:home')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
	template_name = 'profiles/password-reset.html'
	email_template_name = 'profiles/mail/password-reset.html'
	subject_template_name = 'profiles/mail/password-reset-subject.txt'
	success_message = \
		'E-postanıza bir parola kurtarma linki gönderdik. Lütfen kontrol ediniz, '\
		've mesaj almadıysanız tekrar deneyiniz'
	success_url = reverse_lazy('profiles:custom-login')


def logout_view(request):
	logout(request)
	return redirect(to='pets:home')
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.shortcuts import render,redirect
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

from .forms import RegisterForm, LoginForm, UserForm, ProfileForm, VerifyForm
from .models import SignUpRequest

@login_required(login_url='profiles:custom-login')
def profile(request):

	if request.method == 'POST':
		form_user = UserForm(request.POST,instance=request.user)
		form_profile = ProfileForm(request.POST,instance=request.user.profile)

		if form_user.is_valid() and form_profile.is_valid():
			print("valid")
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
			messages.success(request,'Parolanız başarı ile değiştirildii')
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
	if request.method == 'POST':
		form = VerifyForm(request.POST)
		if form.is_valid():
			while True:
				code = secrets.token_hex()
				if SignUpRequest.objects.filter(code=code):
					continue
				break
			sign_up_request = SignUpRequest(email=form.cleaned_data['email'],code=code)
			# sign_up_request.save()
			mail = EmailMessage(
				'Sahiplensene E-posta doğrulama.',
				render_to_string('profiles/mail/verify.html',{
					'link':f'127.0.0.1:8000/profile/verify/{form.cleaned_data["email"]}/{code}'
				}),
				'sahiplenesene.com',
				[form.cleaned_data['email']],
			)
			mail.content_subtype = 'html'
			mail.send()
			messages.success(request,f'E-postanıza ({form.cleaned_data["email"]}) doğrulama linki gönderildi. Kontrol edip geçiş yapınız...')
			form = VerifyForm()

	else:
		form = VerifyForm()

	return render(request,'profiles/verify.html',{'form':form})

def register(request,email,code):
	form_user = UserForm()
	form_profile = ProfileForm()
	return render(request,'profiles/register.html',{'form_user':form_user,'form_profile':form_profile})

class RegisterView(View):
	form_class = RegisterForm
	initial = {'key':'value'}
	template_name = 'profiles/register.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(to='/')

		return super(RegisterView, self).dispatch(request, *args, **kwargs)

	def get(self,request,*args,**kwargs):
		form = self.form_class(initial=self.initial)
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}')

			return redirect(to='/')

		return render(request,self.template_name,{'form':form})


def password_forgot(request):
	return render(request,'profiles/password-forgot.html')


def password_change(request):
	return render(request,'profiles/password-change.html')


def logout_view(request):
	logout(request)
	return redirect(to='/')
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from phonenumber_field.formfields import PhoneNumberField

from .models import Profile,User

DEFAULT_INPUT_ATTRS = {
	'class':'mb-0'
}

class VerifyForm(forms.Form):

	email = forms.EmailField(
		required = True,
		widget = forms.EmailInput(attrs=DEFAULT_INPUT_ATTRS)
	)

class RegisterForm(UserCreationForm):

	first_name = forms.CharField(
		max_length=100,
		required=True,
		widget = forms.TextInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	last_name = forms.CharField(
		max_length=100,
		required=True,
		widget = forms.TextInput(attrs=DEFAULT_INPUT_ATTRS)	
	)
	username = forms.CharField(
		max_length=100,
		required=True,
		widget = forms.TextInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	email = forms.EmailField(
		required=True,
		widget = forms.TextInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	password1 = forms.CharField(
		max_length=50,
		required=True,
		widget=forms.PasswordInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	password2 = forms.CharField(
		max_length=50,
		required=True,
		widget=forms.PasswordInput(attrs=DEFAULT_INPUT_ATTRS)
	)

	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']


class LoginForm(AuthenticationForm):

	username = forms.CharField(
		max_length=100,
		required=True,
		widget = forms.TextInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	password = forms.CharField(
		max_length=50,
		required=True,
		widget=forms.PasswordInput(attrs=DEFAULT_INPUT_ATTRS)
	)
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = User
		fields = ['username','password','remember_me']

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name','password']
		widgets = {	
			'username':forms.TextInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'Kullanıcı adınız'}),
			'email':forms.EmailInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'E-posta'}),
			'first_name':forms.TextInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'Adınız'}),
			'last_name':forms.TextInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'Soyadınız'}),
			'password':forms.PasswordInput(attrs=DEFAULT_INPUT_ATTRS),
		}

class ProfileForm(forms.ModelForm):
	# avatar = forms.ImageField(widget=forms.FileInput(attrs=DEFAULT_INPUT_ATTRS))
	phone = PhoneNumberField(widget=forms.TextInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'Telefon Numarası','type':'tel'}))
	waphone = PhoneNumberField(widget=forms.TextInput(attrs=DEFAULT_INPUT_ATTRS|{'placeholder':'WhatsApp Numarası','type':'tel'}))

	class Meta:
		model = Profile
		fields = ['phone','waphone']

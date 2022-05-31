from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

class SignUpRequest(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=64,unique=True)

    def __repr__(self):
        return f'<SignUpRequest- {self.email} >'

    def __str__(self):
        return f'Hesap Açma İsteği ({self.email})'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True,null=True)
    waphone = PhoneNumberField(blank=True,null=True)

    def __repr__(self):
        return f'<Profile{self.user.username} {self.phone}>'

    def __str__(self):
        return f'Profil ({self.user.username})'
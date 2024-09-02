from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="profile/", default="profile/default.png")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
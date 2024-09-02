from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


# class user(models.Model):
#     name = models.CharField(max_length=50)
#     dept = models.CharField(max_length=50)
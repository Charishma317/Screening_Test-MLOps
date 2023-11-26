# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    display_picture = models.ImageField(upload_to='display_pictures/')
    areas_of_interest = models.ManyToManyField('AreaOfInterest', blank=True)
    about = models.TextField(blank=True)

class AreaOfInterest(models.Model):
    name = models.CharField(max_length=255, unique=True)
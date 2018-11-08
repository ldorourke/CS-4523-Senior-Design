
from django import forms
from django.db import models
from django.forms import ModelForm

# Create your models here.

# we're going to need tables for rooms, courses, professors, and...?

class User(models.Model):
	uname = models.CharField(max_length = 128)
	hashed_pass = models.CharField(max_length = 128)

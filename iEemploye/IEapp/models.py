from django.db import models
from django import forms
from django.core import validators
# Create your models here.
class emp_info(models.Model):
    name=models.CharField(max_length=250, null=True)
    emid=models.CharField(max_length=250, null=True)
    role=models.CharField(max_length=250, null=True)
    join=models.CharField(max_length=250, null=True)
    vry=models.CharField
    
class forms_name(forms.Form):
    vryemail= forms.CharField()
    
class empin(models.Model):
    name=models.TextField(max_length=260)
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class CreateUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
    
class FilesForm(forms.ModelForm):
    class Meta:
        model = files
        fields = '__all__'
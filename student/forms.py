from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	spass=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Student
		fields = '__all__'
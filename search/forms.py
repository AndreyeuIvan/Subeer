from django.forms import ModelForm
from django import forms
from .import models 

class NameForm(forms.ModelForm):
	class Meta:
		model = models.Opinion
		fields = ['BIO', 'Issue', 'Description']


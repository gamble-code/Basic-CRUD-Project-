from .models import UserForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

#Code Starts Here
class Form(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['name', 'email', 'contact', 'expertise']
        labels = {'name': 'Name', 'contact': 'Contact', 'email': 'Email', 'expertise': 'Expertise'}
        widgets = {'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'enter your name'}),
                   'contact': forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'enter your contact details'}),
                   'email': forms.EmailInput(attrs={'class':'form-control' ,'placeholder' : 'enter your email-id'}),
                   'expertise': forms.TextInput(attrs={'class':'form-control' ,'placeholder' : 'enter software language you know'}),}


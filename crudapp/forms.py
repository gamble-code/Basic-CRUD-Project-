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

class SignupForm(UserCreationForm):
    class Meta():
        password2 = forms.CharField(label = 'Confirm- Password', widget= forms.PasswordInput(attrs={'class':'form-control'}))
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name' : 'Last Name', 'email' : 'Email-Id'}
        widgets =  {'username': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'enter a unique username'}),
          'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'enter your first name'}),
        'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'enter your last name'}),
        'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'enter your email-id'}),}
        

class EditUserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username', 'first_name','last_name','email']
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name' : 'Last Name', 'email' : 'Email-Id'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields ='__all__'
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name' : 'Last Name', 'email' : 'Email-Id'}
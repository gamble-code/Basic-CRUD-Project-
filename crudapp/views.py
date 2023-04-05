from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserForm
from .forms import Form
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from .forms import SignupForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib.auth.models import User
# Create your views here.

def data_input(request):
    if request.method == "POST":
        data = Form(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            contact = data.cleaned_data['contact']
            email = data.cleaned_data['email']
            expertise = data.cleaned_data['expertise']
            data_store = UserForm(name = name, contact = contact, email = email, expertise = expertise)
            data_store.save()
            data = Form()
    else:
        data = Form()
    data_details= UserForm.objects.all()
    return render(request,'html/home.html',{'form':data, 'data_output': data_details})

def update_data(request,id):
    if request.method == "POST":
        data = UserForm.objects.get(pk=id)
        form = Form(request.POST, instance = data)
        if form.is_valid:
            form.save()
            messages.SUCCESS(request,'Details Updated Successfully')
    else:
        data = UserForm.objects.get(pk=id)
        form = Form(instance = data)
    return render(request, 'html/update_data.html',{'form':form})

def delete_data(request,id):
    if request.method == "POST":
        data = UserForm.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect("/")


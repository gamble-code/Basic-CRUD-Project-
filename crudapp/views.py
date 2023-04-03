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

def sign_up(request):
    if request.method == "POST":
        data = SignupForm(request.POST)
        if data.is_valid():
            messages.success(request,"Your account has been created successfully.")
            data.save()
    else:
        data = SignupForm()
    return render(request,'html/signup.html',{'form': data})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            data = AuthenticationForm(request=request, data = request.POST)
            if data.is_valid():
                username = data.cleaned_data['username']
                password = data.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request, "Login Successfull.")
                return HttpResponseRedirect('/profile/')
        else:
            data = AuthenticationForm()
        return render(request,'html/userlogin.html',{'form': data})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                data = EditAdminProfileForm(request.POST, instance = request.user)
                users =User.objects.all()
            else:
                data = EditUserProfileForm(request.POST,instance=request.user)
                users = None
            if data.is_valid():
                messages.success(request, "Details Updated.")
                data.save()
        else:
            if request.user.is_superuser == True:
                data = EditAdminProfileForm(instance = request.user)
                users =User.objects.all()
            else:
                data = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'html/userprofile.html',{'name': request.user.username, 'form': data, 'users':users})
    
    else:
        return HttpResponseRedirect('/login/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_changepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data =PasswordChangeForm(user = request.user, data =request.POST)
            if data.is_valid():
                data.save()
                update_session_auth_hash(request,data.user)
                messages.success(request, "Your password changed successfully.")
                return HttpResponseRedirect('/profile/')
        else:
            data =PasswordChangeForm(user = request.user)
        return render(request, 'html/change_pass.html', {'form':data})
    else:
        return HttpResponseRedirect('/login/')
    
def user_detail(request,id):
    if request.user.is_authenticated:
        data = User.objects.get(pk=id)
        data_detail= EditAdminProfileForm(instance=data)
        return render (request, 'html/userdetail.html/', {'form': data_detail})
    else:
        return HttpResponseRedirect('/login/')
from django.contrib import admin
from .models import UserForm

# Register your models here.

@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact', 'expertise']
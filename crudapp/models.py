from django.db import models

# Create your models here.

class UserForm(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length = 50)
    contact = models.IntegerField()
    expertise = models.CharField(max_length=20)
    
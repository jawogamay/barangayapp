from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(null=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Status(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None, null=True)
    location = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    barangay = models.CharField(max_length=200, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.description

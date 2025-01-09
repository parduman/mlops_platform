# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class CustomUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

class InviteCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

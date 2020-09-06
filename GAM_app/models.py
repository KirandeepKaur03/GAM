from django.db import models
from django.contrib.auth.models import User


class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default="", null=True, blank=True)

    def __str__(self):
        return self.email


class Queries(models.Model):
    id = models.AutoField(primary_key=True)
    Message = models.TextField(max_length=255, default="", null=True, blank=True)
    Email = models.EmailField(default="", null=True, blank=True)

    def __str__(self):
        return self.Email


class SiteUser(User):
    address = models.CharField(max_length=255, default="", null=True, blank=True)
    mobile = models.BigIntegerField(default="", null=True, blank=True)


class admins(models.Model):
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255, default="", null=True, blank=True)
    password = models.CharField(max_length=255, default="", null=True, blank=True)

    def __str__(self):
        return self.Username

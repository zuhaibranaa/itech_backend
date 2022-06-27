from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)


class ProfileGroup(models.Model):
    name = models.CharField(max_length=100)


class NAS(models.Model):
    name = models.CharField(max_length=100)

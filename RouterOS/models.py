from django.db import models

# Create your models here.
class NAS(models.Model):
    devicechoices = [
        ('RouterBoard','RouterBoard'),
    ]
    connectivity_type = [
        ('API','API'),
        ('SSH','SSH'),
    ]
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.CharField(max_length=4)
    description = models.TextField()
    version = models.CharField(max_length=20)
    device_type = models.CharField(max_length=255,choices=devicechoices,default=devicechoices[0])
    connectivity_type = models.CharField(max_length=50,choices=connectivity_type)
    
    def __str__(self) -> str:
        return self.name

class ProfileGroup(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    download_rate = models.IntegerField()
    upload_rate = models.IntegerField()
    nas = models.ForeignKey(NAS,models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name

class PPPOE(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nas = models.ForeignKey(NAS,models.CASCADE)
    profile = models.ForeignKey(Profile,models.CASCADE)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField(default=None)
    
    def __str__(self) -> str:
        return self.name
from django.db import models

# Create your models here.
class NAS(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
class ProfileGroup(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    nas = models.ForeignKey(NAS,models.CASCADE)
    model = models.ForeignKey(ProfileGroup,models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

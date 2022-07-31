from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(NAS)
admin.site.register(Profile)
admin.site.register(ProfileGroup)
admin.site.register(PPPOE)
from django.contrib import admin

from Users.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Complain)
admin.site.register(Area)
admin.site.register(SubArea)

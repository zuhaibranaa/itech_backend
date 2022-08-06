from django.contrib import admin

from Users.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Messages)
admin.site.register(Complains)
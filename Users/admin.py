from django.contrib import admin

from Users.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Messages)
admin.site.register(Complains)
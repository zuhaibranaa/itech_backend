from django.contrib import admin

from Users.models import Customer,Manager

# Register your models here.
admin.site.register(Customer)
admin.site.register(Manager)
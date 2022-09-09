from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Supplier)
admin.site.register(BillingAccount)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(InventoryItem)
admin.site.register(Sale)


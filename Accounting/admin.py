from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Suppliers)
admin.site.register(BillingAccounts)
admin.site.register(Invoices)
admin.site.register(Payments)
admin.site.register(InventoryItems)
admin.site.register(Sales)


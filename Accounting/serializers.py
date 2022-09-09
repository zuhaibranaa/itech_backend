from rest_framework import serializers
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'


class BillingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAccounts
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItems
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

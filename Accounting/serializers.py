from rest_framework import serializers
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class BillingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAccount
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

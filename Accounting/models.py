from django.db import models
from Users.models import *
from django.core.validators import RegexValidator

TRANSACTION_CHOICES = (
    ('dr', 'DEBIT'),
    ('cr', 'CREDIT')
)
ACTIVITIES = (
    ('op', 'OPERATING'),
    ('in', 'INVESTING'),
    ('fi', 'FINANCING')
)


# Create your models here.
class Journal(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(max_length=12, choices=ACTIVITIES)
    description = models.TextField(max_length=1000)


class BillingAccount(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    current_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class Transaction(models.Model):
    journal_entry = models.ForeignKey(Journal, models.CASCADE)
    account = models.ForeignKey(BillingAccount, models.CASCADE)
    tx_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.IntegerField()
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.account


class Supplier(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,20}$',
                                 message="Phone number must be entered in the format: '+999999999'")
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.IntegerField(validators=[phone_regex])


class Invoice(models.Model):
    status = {
        (1, 'Paid'),
        (2, 'Pending'),
        (3, 'Overdue'),
    }
    customer_id = models.ForeignKey(User, models.CASCADE, verbose_name='Customer', related_name='Customer')
    generated_by = models.ForeignKey(User, models.CASCADE, verbose_name='Manager', related_name='Manager')
    billing_date = models.DateTimeField(default=None)
    due_date = models.DateTimeField(default=None)
    discount = models.IntegerField(default=None)
    description = models.TextField(max_length=500)
    other_dues = models.IntegerField()
    total_amount = models.IntegerField()
    invoice_status = models.IntegerField(choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()


class Payment(models.Model):
    paid_by = models.ForeignKey(User, models.CASCADE)
    invoice = models.OneToOneField(Invoice, models.CASCADE)
    amount = models.IntegerField()
    method = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()


class InventoryItem(models.Model):
    item_name = models.CharField(max_length=255)
    purchase_price = models.IntegerField()
    sku = models.IntegerField()
    description = models.TextField(max_length=1000)
    buying_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Sale(models.Model):
    item_id = models.ForeignKey(InventoryItem, models.CASCADE)
    quantity = models.IntegerField(default=1)
    sale_price = models.IntegerField()
    payment_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    customer_id = models.ForeignKey(User, models.CASCADE, verbose_name='Customer', related_name='C')

    def __str__(self):
        return self.item_id

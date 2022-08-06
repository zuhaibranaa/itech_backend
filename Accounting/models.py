from django.db import models
from Users.models import *
# Create your models here.

class Invoice(models.Model):
    status = {
        (1, 'Paid'),
        (2, 'Pending'),
        (3, 'Overdue'),
    }
    user_id = models.ForeignKey(User,models.CASCADE,verbose_name='Customer',related_name='Customer')
    generated_by = models.ForeignKey(User,models.CASCADE,verbose_name='Manager',related_name='Manager')
    billing_date = models.DateTimeField(default=None)
    due_date = models.DateTimeField(default=None)
    discount = models.IntegerField(default=None)
    other_dues = models.IntegerField()
    total_amount = models.IntegerField()
    invoice_status = models.IntegerField(choices=status)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Payments(models.Model):
    paid_by = models.ForeignKey(User,models.CASCADE)
    invoice = models.ForeignKey(Invoice,models.CASCADE)
    amount = models.IntegerField()
    method = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return super().__str__()
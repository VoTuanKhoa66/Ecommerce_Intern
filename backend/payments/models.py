from django.db import models
from backend.model import TimeStampedModel
from orders.models import Order
from backend.constant.payment import PaymentMethods, PaymentStatus
# Create your models here.
class Payment(TimeStampedModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, related_name='payment')
    payment_method = models.CharField(max_length=20,choices=PaymentMethods.PAYMENT_METHODS, blank=True, null=True, default=PaymentMethods.CASH)
    status = models.CharField(max_length=20, choices=PaymentStatus.STATUS_PAYMENTS, blank=True, null=True , default=PaymentStatus.PENDING)
    
    class Meta:
        db_table = "Payments"

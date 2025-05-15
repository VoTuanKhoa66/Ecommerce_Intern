from django.db import models
from django.utils import timezone
from backend.model import TimeStampedModel
from users.models import User
from shipping_addresses.models import ShippingAddress
from backend.constant.order import OrderStatus

# Create your models here.
class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=OrderStatus.STATUS_ORDER, blank=True, null=True, default=OrderStatus.PENDING)
    total_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    

    class Meta:
        db_table = "orders"
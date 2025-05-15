from django.db import models
from backend.model import TimeStampedModel
from orders.models import Order
from backend.constant.shipment import ShipmentStatus

# Create your models here.
class Shipment(TimeStampedModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='shipment')
    tracking_number = models.CharField(max_length=20)
    carrier = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=ShipmentStatus.STATUS_SHIPMENT, default=ShipmentStatus.PENDING)

    class Meta:
        db_table = "shipments"
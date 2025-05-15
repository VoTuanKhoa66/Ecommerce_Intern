from django.db import models
from backend.model import TimeStampedModel
from users.models import User
# Create your models here.

class ShippingAddress(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}"
    
    class Meta:
        db_table = "shipping_addresses"
from django.db import models
from backend.model import TimeStampedModel
from orders.models import Order
from products.models import Product

# Create your models here.
class OrderDetail(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='order_details', null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    # product_url_image = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "order_details"
from django.db import models
from backend.model import TimeStampedModel
from categories.models import Category
from brands.models import Brand

# Create your models here.
class Product(TimeStampedModel):
    product_name = models.CharField(max_length=255)
    product_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    product_thumbnail = models.CharField(max_length=255, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    product_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_made = models.CharField(max_length=50, blank=True, null=True)
    product_discount = models.BooleanField(default=False)
    product_discount_start = models.DateTimeField(blank=True, null=True)
    product_discount_end = models.DateTimeField(blank=True, null=True)
    product_sold = models.IntegerField(default=0, null=True, blank=True)
    product_international = models.BooleanField(null=True, blank=True)
    product_rate = models.PositiveIntegerField(default=0, null=True, blank=True)
    product_ingredient = models.TextField(null=True, blank=True)
    product_stock_quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = "products"

    
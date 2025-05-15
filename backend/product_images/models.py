from django.db import models
from backend.model import TimeStampedModel
from products.models import Product
# Sử dụng TimestampModel trong ProductImages model
class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images') 
    image_url = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for product {self.product.id}"

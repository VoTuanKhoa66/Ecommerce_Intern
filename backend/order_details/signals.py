from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import OrderDetail

@receiver(pre_save, sender=OrderDetail)
def save_product_snapshot(sender, instance, **kwargs):
    if instance.product:
        instance.product_name = instance.product.product_name
        instance.product_price = instance.product.product_price
        # instance.product_url_image = instance.product.
from django.db import models
from backend.model import TimeStampedModel

# Create your models here.
class Brand(TimeStampedModel):
    product_image = models.CharField(max_length=255, blank=True, null=True)
    logo_image = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "brands"
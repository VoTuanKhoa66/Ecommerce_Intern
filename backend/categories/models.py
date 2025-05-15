from django.db import models
from backend.model import TimeStampedModel

# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "categories"
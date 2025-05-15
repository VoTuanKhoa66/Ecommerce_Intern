from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'product_image',
            'logo_image',
            'title',
            'discount',
            'created_at', 
            'updated_at'
        ]
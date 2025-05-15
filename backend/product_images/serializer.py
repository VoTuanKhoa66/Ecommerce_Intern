from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id', 
            'product_id',
            'image_url',
            'alt_text',
            'is_primary'
            'created_at',
            'updated_at',
        ]
class ProductImageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image_url',
            'alt_text',
        ]

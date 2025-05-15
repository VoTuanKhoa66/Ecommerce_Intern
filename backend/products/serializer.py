from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializer import CategorySerializer
from brands.models import Brand
from brands.serializer import BrandSerializer
from product_images.serializer import ProductImageShortSerializer

class ProductSerializer(serializers.ModelSerializer):
    product_category_id = serializers.PrimaryKeyRelatedField(        
        queryset=Category.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        source='product_category'
    )
    product_category = CategorySerializer(read_only=True)
    product_brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        source='product_brand'
    )
    product_brand = BrandSerializer(read_only=True)
    product_images = ProductImageShortSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_price',
            'product_thumbnail',
            'product_images',
            'product_type',
            'product_brand',
            'product_brand_id',
            'product_category',
            'product_category_id',
            'product_made',
            'product_discount',
            'product_discount_start',
            'product_discount_end',
            'product_sold',
            'product_international',
            'product_rate',
            'product_ingredient',
            'product_stock_quantity',
            'created_at',
            'updated_at'
        ]

class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price'
        ]
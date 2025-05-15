from rest_framework import serializers
from products.serializer import ProductShortSerializer
from .models import OrderDetail
from products.models import Product
from orders.models import Order
from django.db.models import Sum, F

class OrderDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        source='product'
    )
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        source='order'
    )
    class Meta:
        model = OrderDetail
        fields = [
            'id', 
            'product_id',
            'product_name',
            'product_price',
            'order_id',
            'quantity', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['product_price', 'product_name']

    def create(self, validated_data):
        request = self.context.get('request')
        current_user = request.user if request else None
        order = validated_data.get('order',None)

        
        if order.user != current_user:
            raise serializers.ValidationError("Cannot create order detail for another user.")
        
        if order.status != 'pending':
            raise serializers.ValidationError("Cannot create order detail after the order has been processed.")

        order_detail = super().create(validated_data)

        order.total_price = order.order_details.aggregate(
            total=Sum(F('quantity') * F('product_price'))
        )['total'] or 0

        order.save()

        return order_detail

from rest_framework import serializers
from .models import Payment
from orders.models import Order
from orders.serializer import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset = Order.objects.all(),
        required=True,
        write_only=True,
        source='order'
    )
    order = OrderSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = [
            'id',
            'order',
            'order_id',
            'payment_method',
            'status',
            'created_at', 
            'updated_at'
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        current_user = request.user if request else None 
        order = validated_data.get('order')

        if current_user != order.user:
            raise serializers.ValidationError('You cannot pay for another user.')
        
        validated_data.pop('status',None)
        validated_data['status'] = 'pending'
        try:
            return super().create(validated_data)
        except:
            raise serializers.ValidationError('This order already has a payment.')
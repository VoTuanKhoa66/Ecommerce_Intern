from rest_framework import serializers
from .models import Shipment
from orders.models import Order
from orders.serializer import ShortOrderSerializer

class ShipmentSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset = Order.objects.all(),
        required=True,
        write_only=True,
        source='order'
    )
    order = ShortOrderSerializer(read_only=True)
    class Meta:
        model = Shipment
        fields = [
            'id',
            'order',
            'order_id',
            'tracking_number',
            'carrier',
            'status',
            'created_at', 
            'updated_at'
        ]

    # def create(self, validated_data):
    #     try:
    #         return super().create(validated_data)
    #     except:
    #         raise serializers.ValidationError("This order already has a shipment.")
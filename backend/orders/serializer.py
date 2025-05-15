from rest_framework import serializers
from .models import Order
from users.models import User
from shipping_addresses.models import ShippingAddress
from users.serializer import UserInfoSerializer
from shipping_addresses.serializer import ShippingAddressShortSerializer
from order_details.serializer import OrderDetailSerializer

class OrderSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        source='user'
    )
    shipping_address = ShippingAddressShortSerializer(read_only=True)
    shipping_id = serializers.PrimaryKeyRelatedField(
        queryset=ShippingAddress.objects.all(),
        required=True,
        write_only=True,
        allow_null=True,
        source='shipping_address'
    )
    order_details = OrderDetailSerializer(many=True, read_only=True)
    # payment = PaymentSerializer()
    
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'user_id',
            'status',
            'total_price',
            'shipping_address',
            'shipping_id',
            'order_details',
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['total_price']

    def create(self, validated_data): 
        request = self.context.get("request")
        current_user = request.user if request else None
        shipping_address = validated_data.get('shipping_address', None)
        
        if shipping_address.user != current_user:
            raise serializers.ValidationError("The shipping address does not belong to the current user.")
        
        validated_data['status'] = 'pending'
        validated_data['total_price'] = 0
        validated_data['user_id'] = current_user.id
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user if request else None

        current_status = instance.status
        request_status = validated_data.get('status')
        shipping_address = validated_data.get('shipping_address')

        is_admin = user and user.role and user.role.name == 'admin'
        
        if current_status == 'cancelled':
            raise serializers.ValidationError("Cancelled orders cannot be updated.") 
        
        if current_status == 'pending':
            if not is_admin:
                if request_status != 'cancelled' and request_status is not None:
                    raise serializers.ValidationError("You can only cancel the order.")

                if shipping_address and shipping_address.user != user:
                    raise serializers.ValidationError("The shipping address does not belong to the current user.")
                
                return super().update(instance,{
                    'status': request_status if request_status is not None else instance.status,
                    'shipping_address': shipping_address
                })
            
            if request_status in ['pending', 'cancelled']:
                raise serializers.ValidationError("Admin cannot update to 'pending' or 'cancelled'.")
            
            return super().update(instance, {
                'status': request_status
            })
        
        raise serializers.ValidationError("Can not update after the order has been processed.")
    
class ShortOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'total_price',
            'created_at', 
            'updated_at'
        ]

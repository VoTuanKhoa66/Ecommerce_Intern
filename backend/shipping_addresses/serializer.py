from rest_framework import serializers
from .models import ShippingAddress
from users.serializer import UserInfoSerializer
from users.models import User
 
class ShippingAddressSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        write_only=True,
        allow_null=True,
        source='user'
    )
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'user',
            'user_id',
            'address',
            'city',
            'zip',
            'country',
            'phone',
            'created_at', 
            'updated_at'
        ]
    
    def create(self, validated_data):
        request = self.context.get('request')
        current_user = request.user if request else None
        request_user = validated_data.get('user', None)

        if current_user != request_user:
            raise serializers.ValidationError("Cannot create shipping address for another user.")
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        current_user = request.user if request else None
        request_user = validated_data.get('user', None)

        if current_user != request_user:
            raise serializers.ValidationError("Cannot create shipping address for another user.")
        return super().update(instance, validated_data)

class ShippingAddressShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'address',
            'city',
            'zip',
            'country',
            'phone',
            'created_at', 
            'updated_at'
        ]
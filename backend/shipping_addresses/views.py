from django.shortcuts import render
from backend.views.base import BaseViewSet
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .models import ShippingAddress
from .serializer import ShippingAddressSerializer
# Create your views here.

class ShippingAddressViewSet(BaseViewSet):
    # search_map={
    #     "name" : "icontains",
    #     "description": "icontains"
    # }
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    required_alternate_scopes = {
        "create": [["customer:basic_access"]],
        "update": [["customer:basic_access"]],
        "destroy": [["customer:basic_access"]],
        "retrieve": [["admin:all_manage"],["customer:basic_access"]],
        "list": [["admin:all_manage"],["customer:basic_access"]],
    }

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "admin":
            return ShippingAddress.objects.all()
        
        return ShippingAddress.objects.filter(user__id=user.id)
    


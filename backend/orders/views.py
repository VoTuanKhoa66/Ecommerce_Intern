from django.shortcuts import render
from backend.views.base import BaseViewSet
from rest_framework.exceptions import PermissionDenied
from .models import Order
from .serializer import OrderSerializer

# Create your views here.
class OrderViewSet(BaseViewSet):
    # search_map={
    #     "name" : "icontains",
    #     "description": "icontains"
    # }
    # filter_backends = [ProductFilterBackend]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "admin":
            return Order.objects.all()
        
        return Order.objects.filter(user__id=user.id)
    
    required_alternate_scopes = {
        "create": [["customer:basic_access"]],
        "update": [["admin:all_manage"],["customer:basic_access"]],
        "retrieve": [["admin:all_manage"], ["customer:basic_access"]],
        "list": [["admin:all_manage"], ["customer:basic_access"]],
    }
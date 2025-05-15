from django.shortcuts import render
from backend.views.base import BaseViewSet 
from .models import OrderDetail
from .serializer import OrderDetailSerializer

# Create your views here.
class OrderDetailViewSet(BaseViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "admin":
            return OrderDetail.objects.all()
        
        return OrderDetail.objects.filter(user__id=user.id)

    required_alternate_scopes = {
        "create": [["customer:basic_access"]],
        "retrieve": [["admin:all_manage"], ["customer:basic_access"]],
        "list": [["admin:all_manage"], ["customer:basic_access"]],
    }


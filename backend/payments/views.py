import requests
from django.shortcuts import get_object_or_404, render
from backend.views.base import BaseViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from orders.models import Order
from .serializer import PaymentSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from .momo_payment.create_payment import create_momo_payment
# Create your views here.

class PaymentViewSet(BaseViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    required_alternate_scopes = {
        "create": [["customer:basic_access"]],
        "retrieve": [["admin:all_manage"], ["customer:basic_access"]],
        "list": [["admin:all_manage"], ["customer:basic_access"]],
    }

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == 'admin':
            return Payment.objects.all()
        
        return Payment.objects.filter(order__user=user)
    
    @action(methods=['post'], detail=False, url_path="momo", permission_classes=[IsAuthenticated])
    def momo_payment(self, request, *args, **kwargs):
        user = request.user
        
        if not user.role or user.role.name != 'customer':
            raise Response({"detail": "You do not have permission to make a payment."}, status=status.HTTP_403_FORBIDDEN)

        order_id = request.data.get('order_id')
        order = get_object_or_404(Order, id=order_id)

        return Response(create_momo_payment(order), status=status.HTTP_200_OK)

        
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from backend.views.base import BaseViewSet
from .models import Product
from .serializer import ProductSerializer
from .filter import ProductFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ProductViewSet(BaseViewSet):

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
    
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
    
        headers = self.get_success_headers(serializer.data if not is_many else serializer.data[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    search_map={
        "product_name" : "icontains",
    }
    filter_backends = [ProductFilterBackend]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    required_alternate_scopes = {
        "create": [["admin:all_manage"]],
        "update": [["admin:all_manage"]],
        "destroy": [["admin:all_manage"]],
        "retrieve": [["admin:all_manage"], ["customer:basic_access"]],
        "list": [["admin:all_manage"], ["customer:basic_access"]],
    }

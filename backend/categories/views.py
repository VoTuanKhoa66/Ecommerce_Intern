from django.shortcuts import render
from backend.views.base import BaseViewSet
from .models import Category
from .serializer import CategorySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
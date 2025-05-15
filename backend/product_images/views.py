from rest_framework import status
from rest_framework.response import Response

from backend.views.base import BaseViewSet
from .models import ProductImage
from .serializer import ProductImageSerializer
# from .filter import ProductImageFilterBackend  

class ProductImageViewSet(BaseViewSet):
    search_map = {
        "alt_text": "icontains",
    }

    # filter_backends = [ProductImageFilterBackend]  

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    required_alternate_scope = {
        "create": [["admin:all_manage"]],
        "update": [["admin:all_manage"]],
        "destroy": [["admin:all_manage"]],
        "retrieve": [["admin:all_manage"], ["customer:basic_access"]],
        "list": [["admin:all_manage"], ["customer:basic_access"]],
    }

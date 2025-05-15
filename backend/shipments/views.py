from django.shortcuts import render
from backend.views.base import BaseViewSet
from .models import Shipment
from .serializer import ShipmentSerializer

# Create your views here.
class ShipmentViewSet(BaseViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    required_alternate_scopes = {
        "create": [["admin:all_manage"]],
        "update": [["admin:all_manage"]],
        "destroy": [["admin:all_manage"]],
        "retrieve": [["admin:all_manage"]],
        "list": [["admin:all_manage"]],
    }
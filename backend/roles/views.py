from django.shortcuts import render
from backend.views.base import BaseViewSet
from .models import Role
from .serializer import RoleSerializer

# Create your views here.

class RoleViewSet(BaseViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    required_alternate_scopes = {
        "create": [["admin:all_manage"]],
        "update": [["admin:all_manage"]],
        "destroy": [["admin:all_manage"]],
        "retrieve": [["admin:all_manage"]],
        "list": [["admin:all_manage"]],
    }


from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ShipmentViewSet

# Sử dụng DefaultRouter cho ViewSet
router = SimpleRouter(trailing_slash=False)
router.register(r'shipments', ShipmentViewSet, basename='shipments')

urlpatterns = router.urls
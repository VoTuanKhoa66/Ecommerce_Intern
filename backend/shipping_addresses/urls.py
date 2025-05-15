from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ShippingAddressViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'shipping-addresses', ShippingAddressViewSet, basename='shipping-addresses')
urlpatterns = router.urls
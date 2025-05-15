from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import OrderViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls
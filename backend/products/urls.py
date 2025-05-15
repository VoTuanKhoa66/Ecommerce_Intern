from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ProductViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls
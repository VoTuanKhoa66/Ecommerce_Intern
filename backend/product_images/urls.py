from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ProductImageViewSet
router = SimpleRouter(trailing_slash=False)
router.register(r'product-images', ProductImageViewSet, basename='product_image')
urlpatterns = [
    path('', include(router.urls)),
]

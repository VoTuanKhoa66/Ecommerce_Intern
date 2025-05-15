from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import BrandViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'brands', BrandViewSet, basename='brands')
urlpatterns = router.urls
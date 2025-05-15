from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import CategoryViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, basename='category')
urlpatterns = router.urls
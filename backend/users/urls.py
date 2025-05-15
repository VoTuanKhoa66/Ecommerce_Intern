from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserViewSet

# Sử dụng DefaultRouter cho ViewSet
router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

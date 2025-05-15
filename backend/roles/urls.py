from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import RoleViewSet

# Sử dụng DefaultRouter cho ViewSet
router = SimpleRouter(trailing_slash=False)
router.register(r'roles', RoleViewSet, basename='role')

urlpatterns = router.urls
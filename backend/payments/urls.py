from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PaymentViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'payments', PaymentViewSet, basename='payments')
urlpatterns = router.urls
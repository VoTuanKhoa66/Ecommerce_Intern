from rest_framework.routers import SimpleRouter
from .views import OrderDetailViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'order-details', OrderDetailViewSet)
urlpatterns = router.urls
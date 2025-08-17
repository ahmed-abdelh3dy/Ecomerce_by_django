from rest_framework.routers import DefaultRouter
from .views import OrderViewSets

router = DefaultRouter()
router.register(r'orders', OrderViewSets,  basename='orders')
urlpatterns = router.urls
from .views import ProductViewsets , productImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewsets, basename='products'),
router.register(r'product-images', productImageViewSet, basename='product-images')

urlpatterns = router.urls
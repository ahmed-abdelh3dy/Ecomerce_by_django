from .views import ProductViewsets , productImageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register(r'products', ProductViewsets, basename='products'),
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'images', productImageViewSet, basename='product-images')

urlpatterns = router.urls + products_router.urls




# router.register(r'product-images', productImageViewSet, basename='product-images')

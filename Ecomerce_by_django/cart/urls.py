from .views import CartView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'carts', CartView,  basename='carts')
urlpatterns = router.urls
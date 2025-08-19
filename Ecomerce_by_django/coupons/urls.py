from .views import CouponViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'coupons', CouponViewSets, basename='coupons')

urlpatterns = router.urls
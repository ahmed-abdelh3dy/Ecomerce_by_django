from .views import CategoriesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoriesViewSet, basename='category')
urlpatterns = router.urls
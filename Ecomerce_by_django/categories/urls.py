from .views import CategoriesViewSet ,CategoryImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoriesViewSet, basename='category')
router.register(r'category-image', CategoryImageViewSet, basename='category-images')

urlpatterns = router.urls
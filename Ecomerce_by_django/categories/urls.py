from .views import CategoriesViewSet ,CategoryImageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()

router.register(r'categories', CategoriesViewSet, basename='categories')

category_router = routers.NestedDefaultRouter(router, r'categories', lookup='category')
category_router.register(r'images', CategoryImageViewSet, basename='category-images')

urlpatterns = router.urls + category_router.urls







# router.register(r'category-image', CategoryImageViewSet, basename='category-images')

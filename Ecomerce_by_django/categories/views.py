from rest_framework import viewsets, status
from .models import Categories
from .models import CategoryImage
from .serializers import CategorySerializer
from .serializers import CategoryImageSerializer
from products.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["categories"])
class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]



    def get_queryset(self):
        if self.request.user.role == "admin":
            return Categories.objects.prefetch_related("category_images")
        return Categories.objects.filter(status="active").prefetch_related(
            "category_images"
        )

    def perform_create(self, serializer):
        images = self.request.FILES.getlist("images")
        category = serializer.save()

        for image in images:
            category.category_images.create(image=image)



@extend_schema(tags=["category-images"])
class CategoryImageViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = CategoryImage.objects.all()

    http_method_names = [ 'put', 'delete']


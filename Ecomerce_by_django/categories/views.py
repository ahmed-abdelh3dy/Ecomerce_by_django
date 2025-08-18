from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Categories
from .models import CategoryImage
from .serializers import CategorySerializer
from .serializers import CategoryImageSerializer
from rest_framework.permissions import IsAuthenticated
from products.permissions import IsAdmin
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["categories"])
class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

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

    def perform_update(self, serializer):
        images = self.request.FILES.getlist("images")
        category = serializer.save()

        # Replace old images with new 
        if images:
            category.category_images.all().delete()
            for image in images:
                category.category_images.create(image=image)

        # add new without deleting old
        # for image in images:
        #     category.category_images.create(image=image)

@extend_schema(tags=["category-images"])
class CategoryImageViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryImageSerializer
    queryset = CategoryImage.objects.all()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    # def get_queryset(self):
    #     if self.request.user.role == "admin":
    #         return CategoryImage.objects.prefetch_related("category_images")
    #     return CategoryImage.objects.filter(status="active").prefetch_related(
    #         "category_images"
    #     )

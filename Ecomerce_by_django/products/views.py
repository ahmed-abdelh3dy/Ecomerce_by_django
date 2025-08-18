from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin


@extend_schema(tags=["products"])
class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "tags", "name"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.role == "admin":
            return Products.objects.prefetch_related("product_images")
        return Products.objects.filter(stock__gt=0, status="active").prefetch_related("product_images")


    def perform_create(self, serializer):
        images = self.request.FILES.getlist("images")
        category = serializer.save()

        for image in images:
            category.product_images.create(image=image)

    def perform_update(self, serializer):
        images = self.request.FILES.getlist("images")
        category = serializer.save()

        # Replace old images with new 
        if images:
            category.product_images.all().delete()
            for image in images:
                category.product_images.create(image=image)

        # add new without deleting old
        # for image in images:
        #     category.category_images.create(image=image)

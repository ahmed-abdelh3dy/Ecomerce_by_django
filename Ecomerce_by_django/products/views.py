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

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist("images")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        for image in images:
            product.product_images.create(image=image)

        return Response(
            self.get_serializer(product).data, status=status.HTTP_201_CREATED
        )

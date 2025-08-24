from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products, ProductImages
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsAdminOrReadOnly
from .serializers import ProductImageSerializer


@extend_schema(tags=["products"])
class ProductViewsets(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ["category", "tags"]
    search_fields = ["name", "description"]

    def get_queryset(self):
        role = getattr(self.request.user, "role", None)
        if role == "admin":
            return Products.objects.prefetch_related("product_images")
        return Products.objects.filter(stock__gt=0, status="active").prefetch_related(
            "product_images"
        )

    def perform_create(self, serializer):
        images = self.request.FILES.getlist("images")
        product = serializer.save()

        for image in images:
            product.product_images.create(image=image)


@extend_schema(tags=["product-images"])
class productImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):

        return ProductImages.objects.filter(product=self.kwargs.get("product_pk"))

    http_method_names = ["get", "put", "delete"]

    # metho one
    def get_queryset(self):
        if self.request.user.role == "admin":
            return Products.objects.prefetch_related("product_images")
        return Products.objects.filter(stock__gt=0, status="active").prefetch_related(
            "product_images"
        )

    # method two
    def get_queryset(self):
        role = getattr(self.request.user, "role", None)
        if role == "admin":
            return Products.objects.prefetch_related("product_images")
        return Products.objects.filter(stock__gt=0, status="active").prefetch_related(
            "product_images"
        )

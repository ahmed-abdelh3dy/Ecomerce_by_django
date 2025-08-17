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
    queryset = Products.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "tags" , "name"]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if getattr(self.request.user, 'role', None) == 'admin':
            return Products.objects.all()
        return Products.objects.filter(stock__gt=0 , status = 'active')


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



# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1NTA0NjcyLCJpYXQiOjE3NTU0MTgyNzIsImp0aSI6ImRmMDhiZjNkYjlkNDQwMzU5Mjg1OWQ3OTc1ZWRiZjkyIiwidXNlcl9pZCI6IjMifQ.Ms27vWiW2jJfRkhTw8Wi6p9CEauTIrNDR3yGw3itnbo


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1NTA0NzU5LCJpYXQiOjE3NTU0MTgzNTksImp0aSI6IjRmMzg0MjIxMzNlZjQwYjZiYmRjZGI3YzhmZTcwYmMyIiwidXNlcl9pZCI6IjQifQ.1brA37zTa7eD1mK4cMJWEKG36rt9fgnp2b46Q5egWBU
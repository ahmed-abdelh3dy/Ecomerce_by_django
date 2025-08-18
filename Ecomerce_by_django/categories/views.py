from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Categories
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from products.permissions import  IsAdmin
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['categories'])
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Categories.objects.all()
        return Categories.objects.filter( status = 'active')


    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist("images")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()

        for image in images:
            category.category_images.create(image=image)

        return Response(
            self.get_serializer(category).data, status=status.HTTP_201_CREATED
        )

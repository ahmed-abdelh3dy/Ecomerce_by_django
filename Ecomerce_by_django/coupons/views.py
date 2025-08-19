from django.shortcuts import render
from .serializers import CouponSerializers
from .models import Coupons
from rest_framework import viewsets
from products.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404



@extend_schema(tags=['coupons'])
class CouponViewSets(viewsets.ModelViewSet):
    serializer_class = CouponSerializers
    queryset = Coupons.objects.all()
    permission_classes = [IsAdminOrReadOnly]

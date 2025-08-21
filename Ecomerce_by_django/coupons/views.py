from .serializers import CouponSerializers
from .models import Coupons
from rest_framework import viewsets
from products.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema



@extend_schema(tags=['coupons'])
class CouponViewSets(viewsets.ModelViewSet):
    serializer_class = CouponSerializers
    queryset = Coupons.objects.all()
    permission_classes = [IsAdminOrReadOnly]

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CartSerializer
from .models import Cart
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@extend_schema(tags=["carts"])
class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_update(self, serializer):
    #     instance = serializer.save()
        

    # def partial_update(self, request, *args, **kwargs):
    #     user = request.user
    #     cart_items = Cart.objects.filter(user=user)
    #     quantity = request.data.get("quantity")
    #     product_id = request.data.get("product")

    #     if not cart_items.exists():
    #         return Response(
    #             {"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST
    #         )

    #     for item in cart_items:

    #         cart_item = get_object_or_404(Cart , item.product.id != product_id) 
                
            
    #         product_quantity = item.quantity
    #         product = item.product
    #         print(product_quantity)

    #         update_quantity = quantity + product_quantity
    #         if product.stock < update_quantity:
    #             return Response(
    #                 {"detail": f"Not enough stock for {product.name}"},
    #                 status=status.HTTP_400_BAD_REQUEST,
    #             )

    #         cart_item.quantity = quantity
    #         cart_item.save()

    #     return Response({"quantity updated"}, status=status.HTTP_201_CREATED)

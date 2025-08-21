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
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        cart_item, created = Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:  
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.stock:
                raise serializer.ValidationError({
                    "quantity": f"Requested quantity exceeds available stock"
                })
            cart_item.quantity = new_quantity
            cart_item.save()

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get("product")
        quantity = request.data.get("quantity")

        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)

        product = cart_item.product

        updated_quantity = cart_item.quantity + quantity

        if product.stock < updated_quantity:
            return Response(
                {"message": f"Not enough stock for {product.name}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart_item.quantity = quantity
        cart_item.save()

        return Response(
            {"message": f"Quantity updated to {cart_item.quantity}"},
            status=status.HTTP_200_OK,
        )
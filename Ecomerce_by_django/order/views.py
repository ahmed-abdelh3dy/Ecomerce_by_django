from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Order
from cart.models import Cart
from .serializers import OrderSerializer
from orderitems.models import OrderItems
from drf_spectacular.utils import extend_schema
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from coupons.models import Coupons
from django.shortcuts import get_object_or_404


@extend_schema(tags=["orders"])
class OrderViewSets(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.role == "admin":
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        coupon_code = request.data.get("coupon_code")

        if not cart_items.exists():
            return Response(
                {"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            discount = 0

        if coupon_code:
            coupon = get_object_or_404(Coupons, coupon=coupon_code)
            if coupon and coupon.active == True:
                if coupon.discount_type == "percentage":
                    discount = (total_price * coupon.discount_value) / 100
                elif coupon.discount_type == "fixed":
                    discount = coupon.discount_value

                total_price -= discount
            elif coupon and coupon.active == False:
                return Response({"message": "coupon has been expired"})
            else:
                return Response({"message: the coupon not valid"})

            order = Order.objects.create(
                user=user, total_price=total_price, discount_value=discount
            )

            for item in cart_items:
                product = item.product

                if product.stock < item.quantity:
                    return Response(
                        {"message": f"Not enough stock for {product.name}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                product.stock -= item.quantity
                product.save()

                OrderItems.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    price=product.price,
                )

        cart_items.delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user != user:
            raise PermissionDenied("You can only delete your own orders.")
        instance.delete()

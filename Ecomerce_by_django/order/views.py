from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Order
from cart.models import Cart
from .serializers import OrderSerializer
from orderitems.models import OrderItems
from drf_spectacular.utils import extend_schema
from products.permissions import IsAdminOrReadOnly



@extend_schema(tags=["orders"])
class OrderViewSets(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    
    def get_queryset(self):
        if self.request.user.role == 'admin':
            print(self.request.user.role)
            return Order.objects.all()
        return Order.objects.filter(  user = self.request.user )


    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            return Response(
                {"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            order = Order.objects.create(
                user=user,
                total_price=total_price,
            )

            for item in cart_items:
                product = item.product

                if product.stock < item.quantity:
                    return Response(
                        {"detail": f"Not enough stock for {product.name}"},
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



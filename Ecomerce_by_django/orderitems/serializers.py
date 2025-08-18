from rest_framework import serializers 
from .models import OrderItems

class OrderItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'product_name', 'price', 'quantity']

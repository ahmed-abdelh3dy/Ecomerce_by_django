from .models import Order
from rest_framework import serializers
from orderitems.serializers import OrderItemsSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True, read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'payment_method', 'total_price' ,'order_items' , 'discount_value' ]
        read_only_fields = ['user', 'total_price' ,'discount_value' ]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request and getattr(request.user , 'role' , None) != 'admin':
            fields['status'].read_only = True

        return fields
    
    
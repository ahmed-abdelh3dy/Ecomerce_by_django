from rest_framework import serializers 
from .models import OrderItems

class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id' , 'price' , 'quantity' , 'user' , 'order']
from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id' , 'user' , 'status' , 'created_at' , 'payment_method']
        read_only_fields = ['user','status']

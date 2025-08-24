from rest_framework import serializers
from .models import Cart
from rest_framework.exceptions import ValidationError



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id' , 'user' , 'product' , 'quantity' , 'created_at']
        read_only_fields = ['user' ,]



    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        if quantity > product.stock:
            raise ValidationError({
                "quantity": f"Requested quantity ({quantity}) exceeds available stock ({product.stock})"
            })
        return data    
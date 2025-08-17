from rest_framework import serializers
from .models import Products, ProductImages


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "description",
            "status",
            "tags",
            "price",
            "stock",
            "category",
            "images",
        ]

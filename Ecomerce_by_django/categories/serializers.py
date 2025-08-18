from rest_framework import serializers
from .models import Categories, CategoryImage


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = ["id", "image"]


class CategorySerializer(serializers.ModelSerializer):
    images = CategoryImageSerializer( source = 'category_images' , many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ["id", "name", "description", "status", "images"]

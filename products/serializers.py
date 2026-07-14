from rest_framework import serializers
from products.models import ProductModel


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
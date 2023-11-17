from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName', 'mrp', 'sellPrice', 'hsnCode', 'gstPercent', 'productCategory', 'weight']
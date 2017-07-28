from rest_framework import serializers
from aomswork.models import Product, Color, ProductColor


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','url', 'product_name','product_desc')

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('url', 'color_name')

class ProductColorSerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.product_name')
    color_name = serializers.ReadOnlyField(source='color.color_name')

    class Meta:
        model = ProductColor
        fields = ('url','product_name', 'color_name', 'product', 'color')

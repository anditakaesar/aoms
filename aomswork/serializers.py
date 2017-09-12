from rest_framework import serializers
from aomswork.models import Product, Color, ProductColor, Stock


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

class StockSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        """
        This method check whether the stock is not present then create it
        otherwise update
        """
        stock, created = Stock.objects.update_or_create(
            product_color=validated_data.get('product_color', None),
            defaults={
                'product_color': validated_data.get('product_color', None),
                'ammount': validated_data.get('ammount', None)
            }
        )
        return stock

    class Meta:
        model = Stock
        fields = ('url', 'product_color', 'ammount')

from django.shortcuts import render
from rest_framework import viewsets
from aomswork.models import (
    Product,
    Color,
    ProductColor,
    Stock
)    
from aomswork.serializers import (
    ProductSerializer,
    ColorSerializer,
    ProductColorSerializer,
    StockSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ColorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ProductColorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer

class StockViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

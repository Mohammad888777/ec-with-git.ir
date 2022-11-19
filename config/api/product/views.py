from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):

    serializer_class=ProductSerializer
    queryset=Product.objects.all()
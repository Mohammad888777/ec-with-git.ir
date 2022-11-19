from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet



class CategoryViewset(ModelViewSet):

    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    


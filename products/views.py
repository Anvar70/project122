from django.shortcuts import render
from .serializers import ProductsSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import ProductModel

class ProductsViews(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer

class ProductCreate(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer

class ProductUpdate(RetrieveUpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer

class ProductDelete(RetrieveDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer

class ProductFull(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer
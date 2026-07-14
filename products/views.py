from rest_framework import viewsets
from .models import ProductModel
from .serializers import ProductsSerializer

class ProductsViews(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer
from django.urls import path
from .views import ProductsViews

urlpatterns = [
    path('products/', ProductsViews.as_view({'get': 'list', 'post': 'create'}), name='products'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsViews.as_view()),
    path('product/create/', views.ProductCreate.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdate.as_view()),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view()),
    path('product/<int:pk>/', views.ProductFull.as_view()),
]
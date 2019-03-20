from django.shortcuts import render

# Create your views here.
from database.models import Customer, Order, Product
from .serializers import CustomerSerializer, OrderSerializer, ProductSerializer
from rest_framework import generics


class CustomerView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
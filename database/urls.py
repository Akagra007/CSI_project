from django.urls import path,include
from database.views import CustomerView, CustomerDetails, ProductView, ProductDetails, OrderView, OrderDetails 

urlpatterns = [
    path('customer/', CustomerView.as_view(), name='customer-all'),
    path('customer/<int:pk>/', CustomerDetails.as_view(), name="customer-all-details"),

    path('product/', ProductView.as_view(), name='product-all'),
    path('product/<int:pk>/', ProductDetails.as_view(), name="product-all-details"),

    path('order/', OrderView.as_view(), name='ordre-all'),
    path('order/<int:pk>/', OrderDetails.as_view(), name="order-all-details"), 
]



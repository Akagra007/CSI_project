from django.contrib import admin

# Register your models here.
from database.models import Customer, Order, Product
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
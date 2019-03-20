from rest_framework import serializers
from database.models import Customer, Order, Product

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model= Customer
		fields=('pk','user', 'customer_id', 'customer_street', 
			'customer_street', 'customer_phone','customer_city','customer_zip_code')

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model= Order
		fields=('pk','order_id','cost', 'to_state', 'to_city', 'to_zip_code','address')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model =Product
		fields= ('pk','product_id','product_name', 'product_price')
		
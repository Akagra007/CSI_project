from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Customer(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	customer_id=models.CharField(max_length=16, null=False)
	customer_street=models.CharField(max_length=255, null=False)
	customer_phone=models.CharField(max_length=255, null=False)
	customer_city=models.CharField(max_length=255, null=False)
	customer_zip_code=models.CharField(max_length=6, null=False,  validators=[MinLengthValidator(6)])

	def __str__(self):
		return str(self.customer_id)

class Order(models.Model):
	
	order_id=models.CharField(max_length=16, null=False)
	cost = models.OneToOneField(Customer,on_delete=models.CASCADE)
	
	to_state=models.CharField(max_length=255, null=False)
	to_city=models.CharField(max_length=255, null=False)
	to_zip_code=models.CharField(max_length=6,null=False,  validators=[MinLengthValidator(6)])
	address=models.CharField(max_length=255, null=False)

	def __str__(self):
		return str(self.order_id)

class Product(models.Model):
	
	product_id=models.CharField(max_length=16, null=False)
	product_name=models.CharField(max_length=255, null=False)
	product_price=models.CharField(max_length=255, null=False)

	def __str__(self):
		return str(self.product_id)

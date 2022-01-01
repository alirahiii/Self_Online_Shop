from django.db import models

from Customer.models import Customer
from Product.models import Product



class Order(models.Model):
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE ,related_name='order',null=True,blank=True)
    expiretime=models.TimeField()
    product_id=models.ManyToManyField(Product,related_name="order" )


class Notify(models.Model):
    product_name=models.CharField(max_length=255)
    product_price=models.BigIntegerField()
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE ,related_name='notify',null=True)



from django.db import models

from Product.models import Product
from Customer.models import Customer
class Comment():
    description=models.TextField()
    product_id=models.ForeignKey(Product , on_delete=models.CASCADE , related_name='p_comment')
    Customer_id=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)



from django.db import models
from Account.models import user

class Customer(user):
    image=models.ImageField()
   

class C_address(models.Model):
    address=models.TextField()
    postal_code=models.CharField(max_length=100,unique=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE , related_name='c_addres')

class History(models.Model):
    date_purchesed=models.DateField(auto_now=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='history')
    factor=models.JSONField()



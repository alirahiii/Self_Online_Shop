

from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL
from Salesman.models import seller

class Category(models.Model):
    cat_title=models.CharField(max_length=150)
    sub_cat=models.ForeignKey('self',on_delete=SET_NULL,null=True)
    
    def __str__(self) -> str:
        return self.cat_title


class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(null=True)
    brand=models.CharField(max_length=50,null=True)
    price=models.BigIntegerField(null=True)
    amount=models.IntegerField(null=True)
    actvate=models.BooleanField()
    img1=models.ImageField()
    img2=models.ImageField()
    img3=models.ImageField()
    img4=models.ImageField()
    cat_id=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='product' )
    sellsman_id=models.ForeignKey(seller,on_delete=models.CASCADE ,related_name='product')


    

    def __str__(self) -> str:
        return [self.name , self.brand] 

         

class Property(models.Model):
    property_name=models.CharField(max_length=50,null=True,blank=True)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)



class Details(models.Model):
    pro_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    detail=models.CharField(max_length=400 ,null=True,blank=True) 
    
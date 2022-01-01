
from django.db import models
from Account.models import user


class seller(user):
    image=models.ImageField(null=True,blank=True)
    address=models.TextField()
    postal_code=models.CharField(max_length=10)
  



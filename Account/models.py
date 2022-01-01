from django.db import models
from django.contrib.auth.models import User


class user(User):
    phone_number = models.CharField(max_length=11, verbose_name="phone number")
    img = models.ImageField(upload_to="user/", null=True, blank=True)
    
    class Meta:
        verbose_name = "user"


    def __str__(self) -> str:
         return self.User.username
from django.db import models
from user.models import CustomeUser
from products.models import Products


class Cart(models.Model):
    user = models.ForeignKey(CustomeUser, related_name= 'users' , on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name= 'products' , on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

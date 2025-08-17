from django.db import models
from order.models import Order
from products.models import Products


class OrderItems(models.Model):
    order =models.ForeignKey(Order , related_name='order_items' , on_delete=models.CASCADE)
    product =models.ForeignKey(Products , related_name='product_items' , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


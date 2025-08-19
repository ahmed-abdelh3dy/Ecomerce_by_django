from django.db import models
from user.models import CustomeUser


class Order(models.Model):

    class order_status(models.TextChoices):
        pending = 'pending' , 'Pending'
        shipped = 'shipped' , 'Shipped'
        delivered = 'delivered' , 'Delivered'
        
    user = models.ForeignKey(CustomeUser, related_name='user_orders' , on_delete=models.CASCADE)
    total_price =models.PositiveIntegerField()
    payment_method = models.CharField(default='cash' , editable=False)
    created_at = models.TimeField(auto_now_add=True)
    status = models.CharField(choices=order_status , default=order_status.pending , max_length=10)
    discount_value = models.DecimalField(max_digits=7, decimal_places=2)  


    def __str__(self):
        return self.user.username
    

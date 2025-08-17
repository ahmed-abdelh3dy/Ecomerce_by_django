from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):

    class User_Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    class roles(models.TextChoices):
        customer = "customer", "Customer"
        admin ="admin", "Admin"

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=User_Status , default=User_Status.ACTIVE)
    role = models.CharField(max_length=50, choices=roles , default=roles.customer)
    phone = models.CharField(max_length=11 , unique=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    
    

    def __str__(self):
        return self.username

from django.db import models


class Coupons(models.Model):
    class DiscountType(models.TextChoices):
        PERCENTAGE = "percentage", "Percentage"
        FIXED = "fixed", "Fixed Amount"

    coupon = models.CharField(max_length=20, unique=True)  
    discount_value = models.DecimalField(max_digits=7, decimal_places=2)  
    discount_type = models.CharField(
        max_length=20,
        choices=DiscountType.choices,
        default=DiscountType.PERCENTAGE,
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.coupon

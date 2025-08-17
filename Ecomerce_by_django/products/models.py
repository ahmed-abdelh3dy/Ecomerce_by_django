from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from categories.models import Categories


class Products(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    class Tags(models.TextChoices):
        SALE = "sale", "Sale"
        NEW = "new", "New"

    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )

    category = models.ForeignKey(
        Categories, related_name="products", on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=Status.choices, default=Status.ACTIVE, max_length=10
    )
    tags = models.CharField(choices=Tags.choices, default=Tags.SALE, max_length=10)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to="products_images")

    def __str__(self):
        return f"Image for {self.product.name}"

from django.db import models


class Categories(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField()
    status = models.CharField(
        choices=Status.choices, default=Status.ACTIVE, max_length=10
    )

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="category_images"
    )
    image = models.ImageField(upload_to="categories_images")

    def __str__(self):
        return self.category.name
    

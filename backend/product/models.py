from turtle import title
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self) -> str:
        return self.title

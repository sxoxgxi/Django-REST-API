from turtle import title
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price)*0.8)

    def get_discount(self):
        return self.price * 10/100

    def __str__(self) -> str:
        return self.title

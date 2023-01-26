from django.db import models
from django.contrib.auth.models import User
from products.models import Product, ProductType


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.deletion.SET_NULL, null=True)
    products = models.ManyToManyField(Product)
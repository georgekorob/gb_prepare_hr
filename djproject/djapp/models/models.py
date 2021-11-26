from django.contrib.sites.models import Site
from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    date_add = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, default='RUB')
    provider_name = models.CharField(max_length=64, blank=True)
    categories = models.ManyToManyField(ProductCategory, related_name='categories')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

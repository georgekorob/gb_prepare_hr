from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    date_add = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, default='RUB')
    provider_name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

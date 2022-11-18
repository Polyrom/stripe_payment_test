from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

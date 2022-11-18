from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    price = models.IntegerField(default=0)

    def get_price(self):
        return '{:.2f}'.format(self.price / 100)

    def __str__(self):
        return self.name

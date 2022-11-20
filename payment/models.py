from django.conf import settings
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    price = models.IntegerField(default=0)

    def get_price(self):
        return '$ {:.2f}'.format(self.price / 100.)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.item.name} ({self.quantity})'

    def get_total(self):
        total = self.item.price * self.quantity
        return '$ {:.2f}'.format(total / 100.)


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_template_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.item.price * order_item.quantity
        return '$ {:.2f}'.format(total / 100.)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.item.price * order_item.quantity
        return total

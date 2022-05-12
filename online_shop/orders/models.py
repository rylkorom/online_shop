from django.db import models
from django.utils import timezone
from shop.models import Product


class Order(models.Model):
    """class that represents order's info and status"""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=25)
    email = models.EmailField(default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """class that saves existing order's info"""
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

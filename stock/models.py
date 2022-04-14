from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404

from store.models import Product

class Stock(models.Model):
    product = models.OneToOneField(Product, related_name='product', on_delete=models.RESTRICT)
    available = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    on_order = models.IntegerField(default=0)
    damaged = models.IntegerField(default=0)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

    def get_absolute_url(self):
        return reverse('stock', args=[self.product])

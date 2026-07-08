from django.db import models
from core.models import Base


class Product(Base, models.Model):
    sku = models.CharField('SKU', max_length=20, unique=True, null=True)
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=3000, blank=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField('stock', default=0)
    
    def __str__(self):
        return self.title
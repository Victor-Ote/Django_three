from django.db import models
from core.models import Base


class Product(Base, models.Model):
    sku = models.CharField('SKU', max_length=20, unique=True, blank=True, null=True)
    title = models.CharField('Title', max_length=100, blank=True)
    
    def __str__(self):
        return self.product
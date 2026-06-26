from django.db import models

# Create your models here.

class Base(models.Model):
    create_at = models.DateField('Create_at', auto_now_add=True)
    modifield_at = models.DateField('Modifield_at',auto_now=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        abstract = True
        
        
class Product(Base, models.Model):
    sku = models.CharField('SKU', max_length=20, unique=True, blank=True, null=True)
    title = models.CharField('Title', max_length=100, blank=True)
    
    def __str__(self):
        return self.product
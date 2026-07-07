from django.db import models

# Create your models here.

class Base(models.Model):
    create_at = models.DateField('Create_at', auto_now_add=True)
    modifield_at = models.DateField('Modifield_at',auto_now=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        abstract = True
        
    
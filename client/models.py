from django.db import models
from core.models import Base

class Client(Base, models.Model):
    name = models.CharField('name', max_length=20, unique=True)
    doc_type = models.CharField('doc_type', max_length=20, choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')])
    doc_number = models.CharField('doc_number', max_length=20, unique=True)

    def __str__(self):
        return self.name
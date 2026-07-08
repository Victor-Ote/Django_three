from django.db import models
from core.models import Base

class Client(Base, models.Model):
    name = models.CharField('name', max_length=20)

    def __str__(self):
        return self.name
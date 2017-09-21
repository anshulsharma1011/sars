from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    base_quantity = models.IntegerField(default=1)
    quantity_unit = models.CharField(max_length=20,default='')
    rate = models.CharField(max_length=20,default='')
    photo = models.FileField(blank=True)

    def __str__(self):
        return self.name

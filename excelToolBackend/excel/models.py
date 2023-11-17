from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=200)
    mrp = models.CharField(max_length=100, blank=True)
    sellPrice = models.CharField(max_length=100, blank=True)
    hsnCode = models.CharField(max_length=200, blank=True)
    gstPercent = models.CharField(max_length=10, blank=True)
    productCategory = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=200, blank=True)
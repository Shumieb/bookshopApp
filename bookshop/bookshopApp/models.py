from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

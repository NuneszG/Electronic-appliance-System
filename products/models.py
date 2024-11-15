from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    description = models.TextField()
    durability = models.CharField(max_length=255)

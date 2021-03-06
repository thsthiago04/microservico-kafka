from django.db import models
from uuid import uuid4

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name= models.CharField(max_length=255)
  weight= models.FloatField()

class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  value_order = models.FloatField()
  product = models.OneToOneField(Product, on_delete=models.CASCADE)
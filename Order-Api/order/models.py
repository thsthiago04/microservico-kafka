from django.db import models
from uuid import uuid4

class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  value_order = models.FloatField()

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  order= models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
  name= models.CharField(max_length=255)
  weight= models.FloatField()
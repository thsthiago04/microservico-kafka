from django.db import models
from uuid import uuid4

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  weight = models.FloatField()
  price = models.FloatField()

class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  value_order = models.FloatField()
  product = models.OneToOneField(Product, on_delete=models.CASCADE)
  email = models.EmailField()
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.email
  
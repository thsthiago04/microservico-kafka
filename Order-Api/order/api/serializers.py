from django.db.models import fields
from rest_framework import serializers
from ..models import Order, Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
  product = ProductSerializer(read_only = True)
  
  class Meta:
    model = Order
    fields = ('id', 'value_order', 'product')
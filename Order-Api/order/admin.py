from django.contrib import admin

from .models import Order, Product

@admin.register(Product)
class ProductSerializer(admin.ModelAdmin):
  class Meta:
    model = Product
    fields = (
      'id', 
      'name', 
      'weight', 
      'price'
    )

@admin.register(Order)
class OrderSerializer(admin.ModelAdmin):
  product = ProductSerializer(model=Product, admin_site="product")
  
  class Meta:
    model = Order
    fields = (
      'id', 
      'value_order', 
      'email', 
      'name', 
      'product'
    )
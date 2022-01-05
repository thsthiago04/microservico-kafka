from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Product
from .api.serializers import OrderSerializer

@api_view(['GET', 'POST'])
def order(request):
  if request.method == 'GET':
    orders = Order.objects.all()
    return Response({"results": orders }, status=201)

  if request.method == 'POST':
    order = Order()
    order.value_order = float(request.data['valueOrder'])
    order.save()
    
    product = Product()
    product.name = request.data['valueOrder']

    return Response(OrderSerializer(order).data, status=201)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Product
from .api.serializers import OrderSerializer

@api_view(['GET', 'POST'])
def order(request):
  ordersSerializer = OrderSerializer
  if request.method == 'GET':
    orders = Order.objects.all()
    return Response({"results": ordersSerializer(orders, many=True).data }, status=201)

  if request.method == 'POST':
    product = Product()
    product.name = request.data['name']
    product.weight= request.data['weight']
    product.save()

    order = Order()
    order.value_order = float(request.data['valueOrder'])
    order.product = product
    order.save()

    return Response(OrderSerializer(order).data, status=201)
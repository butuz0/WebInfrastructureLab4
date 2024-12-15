from rest_framework import viewsets
from .serializers import CarSerializer, ClientSerializer, OrderSerializer
from .models import Car, Client, Order


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('client', 'car')
    serializer_class = OrderSerializer

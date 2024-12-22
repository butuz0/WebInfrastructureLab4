from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CarSerializer, ClientSerializer, OrderSerializer
from .models import Car, Client, Order


from rest_framework.parsers import MultiPartParser, FormParser

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    parser_classes = (MultiPartParser, FormParser)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('client', 'car')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'car', 'seller']

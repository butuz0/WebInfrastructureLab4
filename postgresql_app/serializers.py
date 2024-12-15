from rest_framework import serializers
from .models import Car, Client, Order
from mongodb_app.models import Seller


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_type', 'price', 'mileage', 'condition']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'gender', 'email']


class OrderSerializer(serializers.ModelSerializer):
    client_full_name = serializers.ReadOnlyField(source='client.full_name')
    car_type = serializers.ReadOnlyField(source='car.car_type')

    class Meta:
        model = Order
        fields = ['id', 'client', 'client_full_name', 'car', 'car_type', 'seller', 'order_date']

    def validate_seller(self, value):
        if value not in list(Seller.objects.values_list('seller_id', flat=True)):
            raise serializers.ValidationError('You must provide valid seller id')
        return value

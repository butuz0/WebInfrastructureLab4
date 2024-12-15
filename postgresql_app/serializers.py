from rest_framework import serializers
from .models import Car, Client, Order
from mongodb_app.models import Seller
from mongodb_app.serializers import SellerSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_type', 'price', 'mileage', 'condition']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'gender', 'email']


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    car = CarSerializer()
    seller = SellerSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def validate_seller(self, value):
        if value not in list(Seller.objects.values_list('seller_id', flat=True)):
            raise serializers.ValidationError('You must provide valid seller id')
        return value

    def to_representation(self, instance):
        instance.seller = Seller.objects.get(seller_id=instance.seller)
        return super().to_representation(instance)

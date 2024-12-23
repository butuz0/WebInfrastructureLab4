from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend
from mongodb_app.models import Seller
from mongodb_app.serializers import SellerSerializer
from .models import Car, Client, Order

FILE_ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/gif']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_type', 'price', 'mileage', 'condition', 'image']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'gender', 'email', 'image']

    def run_validation(self, data):
        if data.get('image'):
            if data['image'].content_type not in FILE_ALLOWED_TYPES:
                raise serializers.ValidationError({'image': ['Upload a valid image. The file you uploaded was either '
                                                             'not an image or a corrupted image.']})
            data = super().run_validation(data)
            data['image'] = data['image'].read()
            return data
        return super().run_validation(data)


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    seller = serializers.IntegerField(write_only=True)

    client_details = ClientSerializer(read_only=True, source='client')
    car_details = CarSerializer(read_only=True, source='car')
    seller_details = SellerSerializer(read_only=True, source='seller_instance')  # Use the property directly
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'seller', 'car']

    class Meta:
        model = Order
        fields = ['id', 'client', 'car', 'seller', 'client_details', 'car_details', 'seller_details', 'order_date']

    def validate_seller(self, value):
        if not Seller.objects.filter(seller_id=value).exists():
            raise serializers.ValidationError('You must provide a valid seller_id.')
        return value

    def create(self, validated_data):
        seller_id = validated_data.pop('seller')
        order = Order.objects.create(**validated_data, seller=seller_id)
        return order

    def to_representation(self, instance):
        return super().to_representation(instance)

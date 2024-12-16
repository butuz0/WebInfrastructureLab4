from rest_framework import serializers
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_id', 'full_name', 'age', 'gender']
        extra_kwargs = {
            'custom_id': {'required': False},  # Ensure custom_id is not required in the serializer
        }

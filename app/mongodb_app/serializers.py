from rest_framework import serializers
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_id', 'full_name', 'age', 'gender']
        extra_kwargs = {
            'custom_id': {'required': False},  # Ensure custom_id is not required in the serializer
        }

    def create(self, validated_data):
        seller = Seller(**validated_data)
        last_seller = Seller.objects.all().order_by('-seller_id').first()
        seller.seller_id = last_seller.seller_id + 1 if last_seller else 1
        seller.save()
        return seller

    # def update(self, instance, validated_data):
    #     instance = super().update(instance, validated_data)
    #     Seller.objects.filter(seller_id=instance.seller_id).last().delete()
    #     return instance

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Seller
import json

from rest_framework import viewsets
from .serializers import SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'seller_id'

    def validate_seller_id(self, value):
        if value in list(Seller.objects.values_list('seller_id', flat=True)):
            raise serializers.ValidationError('Seller id must be unique')
        return value

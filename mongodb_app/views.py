from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Seller
import json


# Create your views here.
def get_all_sellers(request):
    res = list(Seller.objects.values('seller_id', 'full_name', 'age', 'gender'))
    return JsonResponse(res, safe=False, status=200)


def get_seller(request, seller_id):
    res = Seller.objects.values('seller_id', 'full_name', 'age', 'gender').get(seller_id=seller_id)
    return JsonResponse(res, status=200)


@csrf_exempt
def create_seller(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        seller = Seller.objects.create(
            seller_id=data['seller_id'],
            full_name=data['full_name'],
            age=data['age'],
            gender=data['gender']
        )
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)
    except (ValueError, ValidationError) as e:
        return JsonResponse({'error': f'Wrong field value: {e}'}, status=400)
    else:
        return JsonResponse({
            'seller_id': seller.seller_id,
            'full_name': seller.full_name,
            'age': seller.age,
            'gender': seller.gender
        }, status=201)

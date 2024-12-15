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
    try:
        res = Seller.objects.values('seller_id', 'full_name', 'age', 'gender').get(seller_id=seller_id)
        return JsonResponse(res, status=200)
    except Seller.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)


@csrf_exempt
def create_seller(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))

        if data['seller_id'] in list(Seller.objects.values_list('seller_id', flat=True)):
            return JsonResponse({'error': f'Seller id is already used'}, status=400)

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


@csrf_exempt
def update_seller(request, seller_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)

    try:
        seller = Seller.objects.get(seller_id=seller_id)
        data = json.loads(request.body.decode('utf-8'))
    except Seller.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        for field in data:
            setattr(seller, field, data[field])
        seller.save()

        return JsonResponse({
            'seller_id': seller.seller_id,
            'full_name': seller.full_name,
            'age': seller.age,
            'gender': seller.gender
        }, status=200)


@csrf_exempt
def delete_seller(request, seller_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

    try:
        Seller.objects.get(seller_id=seller_id).delete()
    except Seller.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    else:
        return JsonResponse({'message': 'Deleted successfully'}, status=200)

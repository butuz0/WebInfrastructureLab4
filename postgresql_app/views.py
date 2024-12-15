from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Car, Client, Order
import json


# Create your views here.
def get_all_cars(request):
    res = list(Car.objects.values('id', 'car_type', 'price', 'mileage', 'condition'))
    return JsonResponse(res, safe=False, status=200)


def get_car(request, car_id):
    try:
        res = Car.objects.values('id', 'car_type', 'price', 'mileage', 'condition').get(id=car_id)
        return JsonResponse(res, status=200)
    except Car.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)


@csrf_exempt
def create_car(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))

        car = Car.objects.create(
            car_type=data['car_type'],
            price=data['price'],
            mileage=data['mileage'],
            condition=data['condition']
        )
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)
    except (ValueError, ValidationError) as e:
        return JsonResponse({'error': f'Wrong field value: {e}'}, status=400)
    else:
        return JsonResponse({
            'id': car.id,
            'car_type': car.car_type,
            'price': car.price,
            'mileage': car.mileage,
            'condition': car.condition
        }, status=201)


@csrf_exempt
def update_car(request, car_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)

    try:
        car = Car.objects.get(id=car_id)
        data = json.loads(request.body.decode('utf-8'))
    except Car.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        for field in data:
            setattr(car, field, data[field])
        car.save()

        return JsonResponse({
            'id': car.id,
            'car_type': car.car_type,
            'price': car.price,
            'mileage': car.mileage,
            'condition': car.condition
        }, status=200)


@csrf_exempt
def delete_car(request, car_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

    try:
        Car.objects.get(id=car_id).delete()
    except Car.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    else:
        return JsonResponse({'message': 'Deleted successfully'}, status=200)


def get_all_clients(request):
    res = list(Client.objects.values('full_name', 'age', 'gender', 'email'))
    return JsonResponse(res, safe=False, status=200)


def get_client(request, client_id):
    try:
        res = Client.objects.values('full_name', 'age', 'gender', 'email').get(id=client_id)
        return JsonResponse(res, status=200)
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)


@csrf_exempt
def create_client(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))

        client = Client.objects.create(
            full_name=data['full_name'],
            age=data['age'],
            gender=data['gender'],
            email=data['email']
        )
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)
    except (ValueError, ValidationError) as e:
        return JsonResponse({'error': f'Wrong field value: {e}'}, status=400)
    else:
        return JsonResponse({
            'id': client.id,
            'full_name': client.full_name,
            'age': client.age,
            'gender': client.gender,
            'email': client.email
        }, status=201)


@csrf_exempt
def update_client(request, client_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)

    try:
        client = Client.objects.get(id=client_id)
        data = json.loads(request.body.decode('utf-8'))
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        for field in data:
            setattr(client, field, data[field])
        client.save()

        return JsonResponse({
            'id': client.id,
            'full_name': client.full_name,
            'age': client.age,
            'gender': client.gender,
            'email': client.email
        }, status=200)


@csrf_exempt
def delete_client(request, client_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

    try:
        Client.objects.get(id=client_id).delete()
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Data not found'}, status=404)
    else:
        return JsonResponse({'message': 'Deleted successfully'}, status=200)

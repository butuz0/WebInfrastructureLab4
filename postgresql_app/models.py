from django.db import models
from mongodb_app.models import Seller


class Car(models.Model):
    car_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    condition = models.CharField(max_length=50)


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    email = models.EmailField(null=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.PositiveIntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)

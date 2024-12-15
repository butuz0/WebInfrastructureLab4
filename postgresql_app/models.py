from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    car_type = models.CharField(max_length=50)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    condition = models.CharField(max_length=50)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

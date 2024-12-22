from django.core.exceptions import ValidationError
from django.db import models
from mongodb_app.models import Seller
import uuid
import os
import magic


def upload_to(instance, filename):
    return os.path.join('images/cars', f"{uuid.uuid4()}.{filename.split('.')[-1]}")

def validate_image(value):
    if not magic.Magic(mime=True).from_buffer(value.read()).startswith('image'):
        raise ValidationError("Upload a valid image. The file you uploaded was either not an image or a corrupted image.")

class Car(models.Model):
    car_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to, validators=[validate_image], blank=True, null=True)



class Client(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    email = models.EmailField(null=True)

    image = models.BinaryField(blank=True, null=True, editable=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.PositiveIntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    @property
    def seller_instance(self):
        return Seller.objects.get(seller_id=self.seller)

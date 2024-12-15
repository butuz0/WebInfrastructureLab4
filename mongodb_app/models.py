from djongo import models


class Seller(models.Model):
    _id = models.ObjectIdField()
    seller_id = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    class Meta:
        app_label = 'mongodb_app'

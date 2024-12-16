from djongo import models


class Seller(models.Model):
    seller_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    class Meta:
        app_label = 'mongodb_app'

    def save(self, *args, **kwargs):
        if not self.seller_id:  # If id is not provided, assign a new unique id
            last_seller = Seller.objects.all().order_by('-seller_id').first()
            self.seller_id = last_seller.seller_id + 1 if last_seller else 1
        super(Seller, self).save(*args, **kwargs)

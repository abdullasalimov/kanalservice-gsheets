from django.db import models


class Data(models.Model):
    seq_number = models.IntegerField()
    order_number = models.IntegerField()
    price_usd = models.DecimalField(max_digits=8, decimal_places=2)
    price_rub = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()


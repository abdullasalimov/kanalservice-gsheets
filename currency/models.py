from unicodedata import decimal
from django.db import models


class Data(models.Model):
    order_number = models.CharField(max_length=255, primary_key=True)
    price_usd = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number


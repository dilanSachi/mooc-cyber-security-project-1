from django.db import models
from django.conf import settings

class Item(models.Model):
    item_code = models.CharField(max_length=20)
    price = models.FloatField()
    name = models.CharField(max_length=200)

class Order(models.Model):
    item_code = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_count = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

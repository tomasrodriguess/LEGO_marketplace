from django.db import models
from lego_sets.models import LegoSet
from users.models import User

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=1, decimal_places=1, default=0)

class Listing(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    lego_set = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=30) # e.g., "New", "Used", etc.
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30) #Open, closed, reserved


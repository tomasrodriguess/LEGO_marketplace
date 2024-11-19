from django.db import models
from django.conf import settings
# Create your models here.
from lego_sets.models import LegoSet
from users.models import User

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    public = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s collection of {self.user.username}"

class CollectionItem(models.Model):
    collection  = models.ForeignKey(Collection, on_delete=models.CASCADE)
    lego_set = models.ForeignKey(LegoSet, on_delete=models.CASCADE, to_field='set_number')
    condition = models.CharField(max_length=20)  # e.g., "New", "Used", etc.
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.collection.user.username} | {self.collection.name} - {self.lego_set.name} ({self.condition})"
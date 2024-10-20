from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class LegoSet(models.Model):
    name = models.CharField(max_length=255)
    set_number = models.CharField(max_length=20, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    release_date = models.DateField()
    release_price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.set_number}"
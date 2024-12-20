from rest_framework import serializers
from .models import LegoSet

class LegoSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoSet
        fields = ['set_number','name', 'created_by', 'created_date','release_date','release_price']
        read_only_fields = ['created_by','created_date']

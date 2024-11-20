from rest_framework import serializers
from .models import Listing,Store
from users.models import User


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name','user', 'location', 'rating']
        read_only_fields = ['created_date']

    def validate(self, data):
        if not data['user']:
            raise serializers.ValidationError("User must be specified.")
        elif not User.objects.filter(id=data['user'].id).exists():
            raise serializers.ValidationError({"User": "The specified User does not exist."})
        if Store.objects.filter(user=data['user'].id).exists():
            raise serializers.ValidationError("This user already has a store.")
        return data
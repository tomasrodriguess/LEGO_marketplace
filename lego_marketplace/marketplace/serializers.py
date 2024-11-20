from rest_framework import serializers
from .models import Listing,Store
from users.models import User
from lego_sets.models import LegoSet


class StoreSerializer(serializers.ModelSerializer):
    listings = serializers.SerializerMethodField()
    class Meta:
        model = Store
        fields = ['id','name','user', 'location', 'rating','listings']
        read_only_fields = ['created_date']
    
    def get_listings(self, obj):
        items = Listing.objects.filter(store=obj)
        return ListingSerializer(items, many=True).data

    def validate(self, data):
        if not data['user']:
            raise serializers.ValidationError("User must be specified.")
        elif not User.objects.filter(id=data['user'].id).exists():
            raise serializers.ValidationError({"User": "The specified User does not exist."})
        if Store.objects.filter(user=data['user'].id).exists():
            raise serializers.ValidationError("This user already has a store.")
        return data
    
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id','store','lego_set','visible', 'price', 'condition','status', 'created_date','updated_date']
        read_only_fields = ['created_date','updated_date']

    def validate(self, data):
        if not data['store']:
            raise serializers.ValidationError("Store must be specified.")
        elif not Store.objects.filter(id=data['store'].id).exists():
            raise serializers.ValidationError({"Store": "The specified Store does not exist."})
        if not data['lego_set']:
            raise serializers.ValidationError("LegoSet must be specified.")
        elif not LegoSet.objects.filter(set_number=data['lego_set'].set_number).exists():
            raise serializers.ValidationError({"LegoSet": "The specified LegoSet does not exist."})
        return data
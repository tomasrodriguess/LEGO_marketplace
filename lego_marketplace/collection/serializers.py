from rest_framework import serializers
from .models import Collection, CollectionItem
from lego_sets.serializers import LegoSetSerializer
from lego_sets.models import LegoSet


class CollectionSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Collection
        fields = ['id', 'user', 'name', 'public','description','items']
        read_only_fields = ['user']

    def get_items(self, obj):
        items = CollectionItem.objects.filter(collection=obj)
        return CollectionItemSerializer(items, many=True).data

class CollectionItemSerializer(serializers.ModelSerializer):
    lego_set = serializers.PrimaryKeyRelatedField(queryset=LegoSet.objects.all())  # Accepts the lego_set ID
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    class Meta:
        model = CollectionItem
        fields = ['id', 'collection', 'lego_set', 'condition', 'purchase_date', 'price']
        read_only_fields = ['collection']


    def validate(self, data):
        if not data['lego_set']:
            raise serializers.ValidationError("Lego set must be specified.")
        elif  not LegoSet.objects.filter(set_number=data['lego_set'].set_number).exists():
            raise serializers.ValidationError({"lego_set": "The specified Lego Set does not exist."})
        if not data['collection']:
            raise serializers.ValidationError("Collection must be specified.")
        elif not Collection.objects.filter(id=data['collection'].id).exists():
            raise serializers.ValidationError({"collection": "The specified Collection does not exist."})
        return data

    def update(self, instance, validated_data):
        lego_set_data = validated_data.pop('lego_set', None)
        if lego_set_data:
            LegoSet.objects.update_or_create(defaults=lego_set_data, id=instance.lego_set.id)

        instance.condition = validated_data.get('condition', instance.condition)
        instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
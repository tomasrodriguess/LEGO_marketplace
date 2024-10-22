from rest_framework import serializers
from .models import Collection, CollectionItem
from lego_sets.serializers import LegoSetSerializer
from lego_sets.models import LegoSet


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id', 'user', 'name', 'public','description']
        read_only_fields = ['user']

class CollectionItemSerializer(serializers.ModelSerializer):
    lego_set = LegoSetSerializer()  # Nested serializer for Lego set details

    class Meta:
        model = CollectionItem
        fields = ['id', 'collection', 'lego_set', 'condition', 'purchase_date', 'price']
        read_only_fields = ['collection']

    def create(self, validated_data):
        lego_set_id = validated_data.get('lego_set')
        if not LegoSet.objects.filter(set_number=lego_set_id).exists():
            raise serializers.ValidationError({"lego_set": "The specified Lego Set does not exist."})

        # Validate existence of Collection
        collection = validated_data.get('collection')
        if not Collection.objects.filter(id=collection.id).exists():
            raise serializers.ValidationError({"collection": "The specified Collection does not exist."})

        # Create the CollectionItem
        item = CollectionItem.objects.create(**validated_data)
        item.lego_set = lego_set_id
        item.collection = collection
        item.save()
        return item

    def update(self, instance, validated_data):
        lego_set_data = validated_data.pop('lego_set', None)
        if lego_set_data:
            LegoSet.objects.update_or_create(defaults=lego_set_data, id=instance.lego_set.id)

        instance.condition = validated_data.get('condition', instance.condition)
        instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
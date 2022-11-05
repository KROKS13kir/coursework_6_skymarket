from phonenumber_field import serializerfields
from rest_framework import serializers

from ads.models.ad import Ad



class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'description'
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    phone = serializerfields.PhoneNumberField(source='author.phone', read_only=True)
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id'
        ]
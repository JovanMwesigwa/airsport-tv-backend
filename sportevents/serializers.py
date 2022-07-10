
from rest_framework import serializers

from .models import SportEvent, Category


class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'title', 'subtitle', 'description', 'start_date', 'end_date', 'country',
                  'city', 'country_flag', 'thumbnail', 'event_media', 'category', 'status', 'main', 'isSport')


class SportEventReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'title', 'subtitle', 'description', 'start_date', 'end_date', 'country',
                  'city', 'country_flag', 'thumbnail', 'event_media', 'category', 'status', 'main', 'isSport')
        depth = 2


class SportEventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'thumbnail', 'event_media', )


class SportEventDataOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = ('id', 'title', 'subtitle', 'description', 'start_date', 'end_date', 'country',
                  'city', 'country_flag',  'thumbnail', 'category', 'status', 'main', 'isSport')
        depth = 2


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CategoryReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
    depth = 2

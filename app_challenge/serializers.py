from rest_framework import serializers
from .models import Occurrence, Category


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ('description', 'point', 'category')


class OccurrenceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ('description', 'point', 'category', 'status')


class OccurrenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'category', 'status', 'created_at', 'updated_at',)


class OccurrenceInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'description', 'point', 'category', 'created_at', 'updated_at', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

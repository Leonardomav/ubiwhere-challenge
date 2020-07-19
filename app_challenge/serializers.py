from rest_framework import serializers
from .models import Occurrence, Category


# --- Occurrence Serializers ---

class OccurrenceDefaultSerializer(serializers.ModelSerializer):
    """
    Description:
        Default Occurrence Serializers - Used for POST requests and PUT/PATCH when request.user is not staff
    """

    class Meta:
        model = Occurrence
        fields = ('description', 'point', 'category')


class OccurrenceStaffUpdateSerializer(serializers.ModelSerializer):
    """
    Description:
        Update Occurrence Serializers - Used for PUT/PATCH requests when request.user is staff
    """

    class Meta:
        model = Occurrence
        fields = ('description', 'point', 'category', 'status')


class OccurrenceListSerializer(serializers.ModelSerializer):
    """
    Description:
        List Occurrence Serializers - Used for GET requests
    """

    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'description', 'point', 'category', 'created_at', 'updated_at', 'status')


# --- Category Serializers ---

class CategorySerializer(serializers.ModelSerializer):
    """
    Description:
        Default Serializers
    """
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

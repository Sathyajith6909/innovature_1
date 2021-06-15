from django.urls import path, include
from .models import BooksList
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksList
        fields = ['title', 'price', 'author','category']
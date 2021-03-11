from django.contrib.auth.models import User
from .models import Event
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class EvenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'category', 'date_from', 'date_to', 'description', 'event_image']
from django import forms
from django.forms import ModelForm
from .models import Event, Comment, Participation
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'category', 'date_from', 'date_to', 'description', 'event_image']


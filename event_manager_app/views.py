from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views import generic
from django.urls import reverse_lazy


def AllEventsView(request):
    all_events = Event.objects.all()
    return render(request, 'index.html', {'events': all_events})

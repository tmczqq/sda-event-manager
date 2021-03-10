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


def EventUpdateView(request, id):
    event = get_object_or_404(Event, pk=id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect(AllEventsView)
    return render(request, 'update_event.html', {'form': form})

def EventDeleteView(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == "POST":
        event.delete()
        return redirect(AllEventsView)

    return render(request, 'delete_event.html', {'form': event})

def EventCreateView(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(AllEventsView)
    return render(request, 'create_event.html', {'form': form})


def EventFullView(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, 'event_full_view.html', {'event': event})

def SearchView(request):
    post = request.GET.get('search')
    if post:
        posts = Event.objects.filter(Q(event_name__icontains=post))
    else:
        posts = Event.objects.all().order_by("-date_created")

    return render(request, 'search_event.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Comment
from .forms import EventForm, RegisterForm, CommentForm
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views import generic
from django.urls import reverse_lazy

def EventCreateView(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(AllEventsView)
    return render(request, 'create_event.html', {'form': form})


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


def AllEventsView(request):
    all_events = Event.objects.all()
    return render(request, 'index.html', {'events': all_events})


def EventFullView(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, 'event_full_view.html', {'event': event})


def CatView(request):
    cat = Event.objects.filter(Q(category__icontains=request))

    return render(request, 'category.html', {'events': cat})


def SearchView(request):
    post = request.GET.get('search')
    if post:
        posts = Event.objects.filter(Q(event_name__icontains=post))
    else:
        posts = Event.objects.all().order_by("-date_created")

    return render(request, 'search_event.html', {'posts': posts})


def RegisterView(response):
    if response.method == "POST":
        register = RegisterForm(response.POST)
        if register.is_valid():
            register.save()
        return redirect("read_events")
    else:
        register = RegisterForm()
    return render(response, "registration/register.html", {"form": register})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['id']
        return super().form_valid(form)

    # fields = '__all__'

    # success_url = reverse_lazy("fview_event",kwargs={'id':1})

    def get_success_url(self, **kwargs):
        if kwargs != None:
            return reverse_lazy('fview_event', kwargs={'id': self.kwargs['id']})
        else:
            return reverse_lazy('fview_event', args=(self.object.id,))


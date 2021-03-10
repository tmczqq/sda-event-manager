from django.urls import path
from event_manager_app.views import AllEventsView



urlpatterns = [
    path('index/', AllEventsView, name="read_events"),


]
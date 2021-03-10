from django.urls import path
from event_manager_app.views import AllEventsView



urlpatterns = [
    path('index/', AllEventsView, name="read_events"),
    path('update/<int:id>', EventUpdateView, name="update_event"),
    path('delete/<int:id>', EventDeleteView, name="delete_event"),
    path('create/', EventCreateView, name="create_event"),
    path('fview/<int:id>', EventFullView, name="fview_event"),
    path('search/', SearchView, name="search_event"),

]
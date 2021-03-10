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

class RegisterForm(UserCreationForm):
    male = 'M'
    female = 'F'
    blank = '-'
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    sex = ((male, 'Kobieta'), (female, 'Mężczyzna'), (blank, 'Wybierz płeć'),)
    sex = forms.ChoiceField(choices=sex, required=True, label='Sex')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
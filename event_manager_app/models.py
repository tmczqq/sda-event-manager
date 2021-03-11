from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Category():
    INNE = 0
    KINO = 1
    TEATR = 2
    KONCERT = 3
    CATEGORY_EVENT = (
        (INNE, 'Inne'),
        (KINO, 'Kino'),
        (TEATR, 'Teatr'),
        (KONCERT, 'Koncert'),
    )


class Event(models.Model):
    event_name = models.CharField(validators=[MinLengthValidator(4)], max_length=50, blank=False, unique=True)
    category = models.IntegerField(choices=Category.CATEGORY_EVENT, default=0)
    date_from = models.DateTimeField(null=True, blank=True, default=None)
    date_to = models.DateTimeField(null=True, blank=True, default=None)
    description = models.TextField(validators=[MinLengthValidator(40)], max_length=500, blank=False)
    event_image = models.ImageField(upload_to="event_image", height_field=600, width_field=500, max_length=1000,
                                    null=True, blank=True)

    def __str__(self):
        return self.event_date()

    def event_date(self):
        return "{} ({} - {})".format(self.event_name, self.date_from,self.date_to)


class Comment(models.Model):
    # TODO: Change post to event
    post = models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.event_name, self.name)



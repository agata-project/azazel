from django.db import models
from .event import Event


class Talk(models.Model):
    date = models.DateField()
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    finish_time = models.DateField()
    init_time = models.DateField()
    local = models.TextField()
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)


class Workshop(Talk):
    donate = models.BooleanField(default=False)


class Keynote(Talk):
    pass

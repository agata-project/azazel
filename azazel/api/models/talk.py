from django.db import models
from .event import Event


class Talk(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    description = models.TextField()
    local = models.TextField()
    init_time = models.DateField()
    finish_time = models.DateField()
    date = models.DateField()

class Workshop(Talk):
    donate = models.BooleanField(default=False)

class Keynote(Talk):
    pass

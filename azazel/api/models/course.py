from django.db import models


class Course(models.Model):
    initials = models.CharField(max_length=5)
    name = models.CharField(max_length=50)

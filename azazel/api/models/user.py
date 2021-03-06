from django.db import models
from .course import Course


class User(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default='')
    cpf = models.CharField(max_length=15)
    registration = models.CharField(max_length=15)

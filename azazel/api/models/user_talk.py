from django.db import models
from .user import User
from .talk import Talk


class UserTalk(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

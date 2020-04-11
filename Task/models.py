from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Notes(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

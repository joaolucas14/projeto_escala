# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import time


class Missa(models.Model):
    HORARIOS_CHOICES = [
        (time(7, 0), "7:00"),
        (time(9, 0), "9:00"),
        (time(19, 0), "19:00"),
    ]
    data = models.DateField()
    horario = models.TimeField(choices=HORARIOS_CHOICES)
    pessoas = models.ManyToManyField(User, related_name='missas')

    def __str__(self):
        return f'{self.data.strftime("%Y-%m-%d")} {self.horario.strftime("%H:%M")}'

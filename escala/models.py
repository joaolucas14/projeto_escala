# myapp/models.py
from django.db import models
# from django.contrib.auth.models import User
from datetime import time
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class UsuarioCustomizado(AbstractUser):
    enfermos = models.IntegerField(default=0, verbose_name="Número de enfermos atendidos")
    # Adicione aqui os campos adicionais

    def __str__(self):
        return self.username
    
    
class Missa(models.Model):
    HORARIOS_CHOICES = [
        (time(7, 0), "7:00"),
        (time(9, 0), "9:00"),
        (time(19, 0), "19:00"),
    ]
    data = models.DateField()
    horario = models.TimeField(choices=HORARIOS_CHOICES)
    pessoas = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='missas'
        )

    def __str__(self):
        return f'{self.data.strftime("%Y-%m-%d")} {self.horario.strftime("%H:%M")}'



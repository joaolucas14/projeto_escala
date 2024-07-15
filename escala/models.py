from django.db import models


class Ministro(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    sobrenome = models.CharField(max_length=25, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=True)
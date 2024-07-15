from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .models import Ministro
# Create your views here.


class Home(TemplateView):
    template_name = "escala/home.html"


class Login(LoginView):
    model = Ministro
    fields = [
        "nome",
        "sobrenome",
        "telefone",
        "email",
    ]
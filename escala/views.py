from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CustomLoginForm, RegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class Home(TemplateView):
    template_name = "escala/home.html"


class Teste(TemplateView):
    template_name = "escala/teste.html"


class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return super().form_invalid(form)
    

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
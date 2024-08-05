from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CustomLoginForm, RegisterForm, MissaForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Missa
from django.contrib.auth.mixins import LoginRequiredMixin

class Inicio(TemplateView):
    template_name = "escala/inicio.html"


class Agenda(LoginRequiredMixin, ListView):
    model = Missa
    template_name = 'escala/agenda.html'
    context_object_name = 'missas'

    def get_queryset(self):
        user = self.request.user
        return Missa.objects.filter(pessoas=user).prefetch_related('pessoas')


class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('agenda')  

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


class RegistroMissa(LoginRequiredMixin, CreateView):
    model = Missa
    template_name = 'registration/cadastro_missa.html'
    form_class = MissaForm
    success_url = reverse_lazy('agenda')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['data'].widget.attrs.update({'type': 'date'})
        form.fields['horario'].widget.choices = [(choice.strftime('%H:%M:%S'), label) for choice, label in Missa.HORARIOS_CHOICES]
        form.fields['pessoas'].queryset = User.objects.all()
        return form

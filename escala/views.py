from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from .forms import CustomLoginForm, RegisterForm, MissaForm, PerfilForm
from django.views.generic.edit import CreateView
from .models import Missa
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UsuarioCustomizado


class Inicio(TemplateView):
    template_name = "escala/inicio.html"


class Agenda(LoginRequiredMixin, ListView):
    model = Missa
    template_name = 'escala/agenda.html'
    context_object_name = 'missas'

    def get_queryset(self):
        user = self.request.user
        return Missa.objects.filter(pessoas=user).prefetch_related('pessoas')


class EscalaGeral(LoginRequiredMixin, ListView):
    model = Missa
    template_name = 'escala/escala_geral.html'
    context_object_name = 'missas'


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
    model = UsuarioCustomizado
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
        form.fields['horario'].widget.choices = [
            (choice.strftime('%H:%M:%S'), label)
            for choice, label in Missa.HORARIOS_CHOICES
            ]
        return form


class EditarMissa(LoginRequiredMixin, UpdateView):
    model = Missa
    form_class = MissaForm
    template_name = 'registration/editar_missa.html'
    success_url = reverse_lazy('agenda')

   
class Perfil(LoginRequiredMixin, UpdateView):
    model = UsuarioCustomizado
    form_class = PerfilForm
    template_name = 'perfil/perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        return self.request.user
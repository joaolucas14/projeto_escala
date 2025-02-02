from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Missa
from .models import UsuarioCustomizado
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuário'
            }),
        label="Usuário"
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Senha'
            }),
        label="Senha")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = UsuarioCustomizado
        fields = [
            'username', 'email', 'password1', 'password2', 'enfermos'
            ]
        labels = {
            'username': 'Usuário',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
            'enfermos': 'Quantidade de enfermos atendidos'
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirmar Senha'
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''
            field.label = self.Meta.labels.get(field_name, field.label)


class MissaForm(forms.ModelForm):
    class Meta:
        model = Missa
        fields = ['data', 'horario', 'pessoas']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.Select(),
            'pessoas': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '10',
                'style': 'width: 100%;',
                'aria-label': 'Select people for the Mass',
                'placeholder': 'Choose people',
            }),  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('data', css_class='form-control'),
            Field('horario', css_class='form-control'),
            Field('pessoas', css_class='form-control'),
        )
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        pessoas = cleaned_data.get('pessoas')
        horario = cleaned_data.get('horario')

        for pessoa in pessoas:
           
            if Missa.objects.filter(
                data=data, pessoas=pessoa
                ).exclude(horario=horario).exists():
                raise ValidationError(
                    _('A pessoa %(pessoa)s já está escalada em outra missa no mesmo dia.'),
                    code='invalid',
                    params={'pessoa': pessoa.username},
                )

        return cleaned_data


class PerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'email', 'first_name', 'last_name', 'enfermos']
        labels = {
            'username': 'Usuário',
            'email': 'Email',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'enfermos': "Número de enfermos atendidos"
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm', 'style': 'width: 50%;'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm', 'style': 'width: 50%;'
                }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm', 'style': 'width: 50%;'
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm', 'style': 'width: 50%;'
                }),
            'enfermos': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'style': 'width: 50%;',
            }),
        }

        
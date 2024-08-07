from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Missa
from .models import UsuarioCustomizado


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}), label="Senha")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    additional_field_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Additional Field 1'}))
    additional_field_2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Additional Field 2'}))

    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'email', 'password1', 'password2', 'additional_field_1', 'additional_field_2']
        labels = {
            'username': 'Usuário',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
            'additional_field_1': 'Additional Field 1',
            'additional_field_2': 'Additional Field 2',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'}),
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

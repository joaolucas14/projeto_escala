from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}), label="Senha")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuário',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
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
            # Esta linha abaixo garante que os labels personalizados sejam aplicados
            field.label = self.Meta.labels.get(field_name, field.label)

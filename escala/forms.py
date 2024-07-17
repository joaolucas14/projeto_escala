from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Senha'}), label="Senha")

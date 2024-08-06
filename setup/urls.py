from django.contrib import admin
from django.urls import path
from escala.views import Inicio, CustomLoginView, RegisterView, RegistroMissa, Agenda, EscalaGeral
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("agenda", Agenda.as_view(), name="agenda"),
    path("escala_geral", EscalaGeral.as_view(), name="escala_geral"),
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("registro/", RegisterView.as_view(), name="registro"),
    path("cadastro_missa/", RegistroMissa.as_view(), name="cadastro_missa"),
]

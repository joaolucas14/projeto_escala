from django.contrib import admin
from django.urls import path
from escala.views import Home, CustomLoginView, RegisterView, Teste

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("teste/", Teste.as_view(), name="teste"),
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", RegisterView.as_view(), name="registro"),
]

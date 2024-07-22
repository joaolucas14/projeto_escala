from django.contrib import admin
from django.urls import path
from escala.views import Inicio, CustomLoginView, RegisterView, Home
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("home", Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("registro/", RegisterView.as_view(), name="registro"),
]

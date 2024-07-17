from django.contrib import admin
from django.urls import path
from escala.views import Home, CustomLoginView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
]

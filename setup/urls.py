from django.contrib import admin
from django.urls import path
from escala.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
]

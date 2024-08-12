# escala/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustomizado, Missa


class UsuarioCustomizadoAdmin(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['username', 'email', 'is_staff', 'enfermos']
    

class MissaAdmin(admin.ModelAdmin):
    list_display = ['data', 'horario']
    filter_horizontal = ('pessoas',)


admin.site.register(UsuarioCustomizado, UsuarioCustomizadoAdmin)
admin.site.register(Missa, MissaAdmin)


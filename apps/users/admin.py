from django.contrib import admin
from .models import Perfil


# Personalizando modelos en el admin
class PerfilAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "user","usuario","telefono","direccion", "edad","fecha_nacimiento",
        "genero", )
# Register your models here.
admin.site.register(Perfil, PerfilAdmin)


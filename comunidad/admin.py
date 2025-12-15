
from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("videojuego", "accesorio", "autor", "usuario", "calificacion", "creado")
    search_fields = ("videojuego", "accesorio", "autor", "comentario", "usuario__username")
    list_filter = ("calificacion", "creado")

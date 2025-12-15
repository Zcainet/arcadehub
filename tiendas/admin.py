
from django.contrib import admin
from .models import Sucursal

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "ciudad", "telefono", "activo")
    list_filter = ("pais", "activo")
    search_fields = ("nombre", "pais", "ciudad", "direccion")
    exclude = ("latitud", "longitud")

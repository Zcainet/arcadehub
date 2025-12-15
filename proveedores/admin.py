from django.contrib import admin
from .models import PropuestaProveedor

@admin.register(PropuestaProveedor)
class PropuestaProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre_proveedor", "creado")
    search_fields = ("nombre_proveedor", "mensaje")
    list_filter = ("creado",)

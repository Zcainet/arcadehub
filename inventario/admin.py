from django.contrib import admin
from django import forms

from .models import Categoria, Consola, Producto, ResenaProducto


class ProductoAdminForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    def clean(self):
        cleaned = super().clean()

        # Solo aplicar lógica si el modelo realmente tiene esos campos
        if "es_videojuego" in self.fields and "consola" in self.fields:
            es_videojuego = cleaned.get("es_videojuego")
            consola = cleaned.get("consola")

            # Si NO es videojuego, no forzamos consola y la limpiamos para evitar confusiones
            if es_videojuego is False:
                cleaned["consola"] = None

            # Si ES videojuego, consola puede ser opcional (como tú quieres)
            # Si lo quieres obligatorio:
            # if es_videojuego and not consola:
            #     self.add_error("consola", "Selecciona una consola para el videojuego.")

        return cleaned


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


@admin.register(Consola)
class ConsolaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoAdminForm
    search_fields = ("nombre", "descripcion")
    ordering = ("-id",)  # evita fallar si "creado" no existe

    # --- Helpers (callables) para que list_display nunca reviente ---
    @admin.display(boolean=True, description="¿Videojuego?")
    def es_videojuego_col(self, obj):
        if hasattr(obj, "es_videojuego"):
            return bool(getattr(obj, "es_videojuego"))
        # fallback: si tiene consola, probablemente es videojuego
        if hasattr(obj, "consola") and getattr(obj, "consola") is not None:
            return True
        return False

    @admin.display(description="Precio")
    def precio_col(self, obj):
        # intenta encontrar un campo de precio típico
        for name in ("precio", "precio_venta", "precio_publico", "costo"):
            if hasattr(obj, name):
                return getattr(obj, name)
        return "-"

    # --- Esto hace que admin se adapte a tus campos reales ---
    def get_list_display(self, request):
        fields = {f.name for f in self.model._meta.fields}

        base = ["nombre"]

        if "categoria" in fields:
            base.append("categoria")

        # videojuego/consola
        if "es_videojuego" in fields:
            base.append("es_videojuego")
        else:
            base.append("es_videojuego_col")

        if "consola" in fields:
            base.append("consola")

        # precio
        if "precio" in fields:
            base.append("precio")
        else:
            base.append("precio_col")

        if "existencia" in fields:
            base.append("existencia")

        return tuple(base)

    def get_list_filter(self, request):
        fields = {f.name for f in self.model._meta.fields}
        filtros = []
        if "categoria" in fields:
            filtros.append("categoria")
        if "consola" in fields:
            filtros.append("consola")
        if "activo" in fields:
            filtros.append("activo")
        return tuple(filtros)

    def get_list_editable(self, request):
        # Solo dejar como editable lo que exista y lo que también esté en list_display
        fields = {f.name for f in self.model._meta.fields}
        display = set(self.get_list_display(request))
        editables = []

        for f in ("costo", "existencia", "activo"):
            if f in fields and f in display:
                editables.append(f)


        return tuple(editables)


@admin.register(ResenaProducto)
class ResenaProductoAdmin(admin.ModelAdmin):
    list_display = ("producto", "usuario", "calificacion", "creado")
    list_filter = ("calificacion", "creado")
    search_fields = ("producto__nombre", "usuario__username", "comentario")

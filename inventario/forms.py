
from django import forms
from .models import ResenaProducto

class ResenaProductoForm(forms.ModelForm):
    class Meta:
        model = ResenaProducto
        fields = ["calificacion", "comentario"]

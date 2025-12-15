from django import forms
from .models import PropuestaProveedor

class PropuestaProveedorForm(forms.ModelForm):
    class Meta:
        model = PropuestaProveedor
        fields = ["nombre_proveedor", "mensaje", "archivo_productos"]

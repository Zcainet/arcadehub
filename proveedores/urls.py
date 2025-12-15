from django.urls import path
from .views import contacto_proveedor, contacto_ok

urlpatterns = [
    path("", contacto_proveedor, name="proveedores_contacto"),
    path("ok/", contacto_ok, name="proveedores_contacto_ok"),
]

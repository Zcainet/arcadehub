
from django.urls import path
from .views import lista, crear, editar, eliminar

urlpatterns = [
    path("", lista, name="comunidad_lista"),
    path("nuevo/", crear, name="comunidad_crear"),
    path("editar/<int:pk>/", editar, name="comunidad_editar"),
    path("eliminar/<int:pk>/", eliminar, name="comunidad_eliminar"),
]

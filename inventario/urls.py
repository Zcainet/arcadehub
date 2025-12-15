
from django.urls import path
from .views import catalogo, detalle_producto

urlpatterns = [
    path("", catalogo, name="catalogo"),
    path("p/<int:pk>/", detalle_producto, name="producto_detalle"),
]

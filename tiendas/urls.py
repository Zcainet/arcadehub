
from django.urls import path
from .views import sucursales

urlpatterns = [
    path("", sucursales, name="sucursales"),
]

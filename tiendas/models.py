
from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=120)
    pais = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=40, blank=True)
    horario = models.CharField(max_length=120, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ["pais", "ciudad", "nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.ciudad}, {self.pais})"

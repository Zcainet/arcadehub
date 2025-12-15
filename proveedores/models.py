from django.db import models

class PropuestaProveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=120)
    mensaje = models.TextField()
    archivo_productos = models.FileField(upload_to="propuestas/")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Propuesta de proveedor"
        verbose_name_plural = "Propuestas de proveedores"
        ordering = ["-creado"]

    def __str__(self):
        return self.nombre_proveedor

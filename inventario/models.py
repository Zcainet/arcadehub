from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Consola(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "Consola"
        verbose_name_plural = "Consolas"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="productos")
    consola = models.ForeignKey(
        Consola,
        on_delete=models.SET_NULL,
        related_name="productos",
        null=True,
        blank=True,
    )
    es_videojuego = models.BooleanField(default=False)
    nombre = models.CharField(max_length=120)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.nombre} ({self.consola})" if self.consola else self.nombre

    @property
    def precio(self):
        return self.costo


class ResenaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="resenas")
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="resenas_producto")
    calificacion = models.PositiveSmallIntegerField(default=5)
    comentario = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reseña de producto"
        verbose_name_plural = "Reseñas de productos"
        ordering = ["-creado"]
        unique_together = ("producto", "usuario")

    def __str__(self):
        return f"{self.producto} - {self.usuario}"

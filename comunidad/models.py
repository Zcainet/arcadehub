from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='comentarios')
    videojuego = models.CharField(max_length=120)
    accesorio = models.CharField(max_length=120, blank=True)
    autor = models.CharField(max_length=80)
    comentario = models.TextField()
    calificacion = models.PositiveSmallIntegerField(default=5)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.videojuego} - {self.autor}"

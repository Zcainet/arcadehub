from django.shortcuts import render
from inventario.models import Producto, Categoria

def inicio(request):
    destacados = (
        Producto.objects
        .filter(existencia__gt=0)
        .order_by("-existencia", "-costo")[:4]
    )
    categorias = Categoria.objects.all().order_by("nombre")[:6]
    return render(request, "paginas/inicio.html", {
        "destacados": destacados,
        "categorias": categorias,
    })
    

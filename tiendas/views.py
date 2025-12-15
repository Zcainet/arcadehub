
from django.shortcuts import render
from .models import Sucursal

def sucursales(request):
    items = Sucursal.objects.filter(activo=True)
    q = request.GET.get("q", "").strip()
    if q:
        items = items.filter(
            nombre__icontains=q
        ) | items.filter(pais__icontains=q) | items.filter(ciudad__icontains=q)
    return render(request, "tiendas/sucursales.html", {"sucursales": items, "q": q})

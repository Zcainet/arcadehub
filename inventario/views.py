from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Producto, ResenaProducto
from .forms import ResenaProductoForm


def catalogo(request):
    q = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria")

    productos = Producto.objects.filter(activo=True)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)


    if q:
        productos = productos.filter(
            Q(nombre__icontains=q) |
            Q(descripcion__icontains=q) |
            Q(categoria__nombre__icontains=q) |
            Q(consola__nombre__icontains=q)
        )

    return render(request, "inventario/catalogo.html", {
        "productos": productos,
        "q": q,
        "categoria_id": categoria_id,
    })


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, activo=True)

    resenas = ResenaProducto.objects.filter(producto=producto).select_related("usuario").order_by("-creado")
    promedio = resenas.aggregate(avg=Avg("calificacion"))["avg"]

    ya = None
    if request.user.is_authenticated:
        ya = ResenaProducto.objects.filter(producto=producto, usuario=request.user).first()

    # Solo clientes pueden reseñar
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"{reverse('cliente_login')}?next={request.path}")
        if request.user.is_staff or request.user.is_superuser:
            return HttpResponseForbidden("Solo clientes pueden calificar o comentar productos desde el sitio.")

        form = ResenaProductoForm(request.POST, instance=ya)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.producto = producto
            obj.usuario = request.user
            obj.save()
            return redirect("producto_detalle", pk=producto.id)
    else:
        form = ResenaProductoForm(instance=ya)

    return render(request, "inventario/detalle.html", {
        "producto": producto,
        "resenas": resenas,
        "promedio": promedio,
        "form": form,
        "ya": ya,
    })

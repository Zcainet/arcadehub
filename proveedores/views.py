from django.shortcuts import render, redirect
from .forms import PropuestaProveedorForm

def contacto_proveedor(request):
    if request.method == "POST":
        form = PropuestaProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("proveedores_contacto_ok")
    else:
        form = PropuestaProveedorForm()
    return render(request, "proveedores/contacto.html", {"form": form})

def contacto_ok(request):
    return render(request, "proveedores/ok.html")

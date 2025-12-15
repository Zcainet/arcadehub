
def _deny_staff(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm

def lista(request):
    comentarios = Comentario.objects.all()
    return render(request, "comunidad/lista.html", {"comentarios": comentarios})

@login_required
def crear(request):
    if _deny_staff(request.user):
        return HttpResponseForbidden('Solo clientes pueden publicar en la comunidad.')

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.usuario = request.user
            c.autor = c.autor or request.user.username
            c.save()
            return redirect("comunidad_lista")
    else:
        form = ComentarioForm(initial={"autor": request.user.username})
    return render(request, "comunidad/crear.html", {"form": form})

def _can_edit(user, comentario: Comentario) -> bool:
    return user.is_staff or (comentario.usuario_id == user.id)

@login_required
def editar(request, pk):
    if _deny_staff(request.user):
        return HttpResponseForbidden('Solo clientes pueden editar comentarios desde el sitio.')

    c = get_object_or_404(Comentario, pk=pk)
    if not _can_edit(request.user, c):
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=c)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = c.usuario
            obj.save()
            return redirect("comunidad_lista")
    else:
        form = ComentarioForm(instance=c)
    return render(request, "comunidad/editar.html", {"form": form, "c": c})

@login_required
def eliminar(request, pk):
    if _deny_staff(request.user):
        return HttpResponseForbidden('Solo clientes pueden eliminar comentarios desde el sitio.')

    c = get_object_or_404(Comentario, pk=pk)
    if not _can_edit(request.user, c):
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
    if request.method == "POST":
        c.delete()
        return redirect("comunidad_lista")
    return render(request, "comunidad/eliminar.html", {"c": c})

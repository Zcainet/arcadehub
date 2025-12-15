from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ClienteAuthForm, ClienteRegistroForm


class ClienteLoginView(LoginView):
    template_name = "clientes/login.html"
    # Si ya está logueado, normalmente lo mandamos al inicio.
    # Si prefieres que siempre muestre el login, cambia a False.
    redirect_authenticated_user = False
    authentication_form = ClienteAuthForm

    def get_success_url(self):
        # Si viene ?next=..., respétalo. Si no, manda al inicio.
        return self.get_redirect_url() or reverse_lazy("inicio")


class ClienteLogoutView(LogoutView):
    # Logout por POST (más seguro y compatible)
    http_method_names = ["post", "options"]
    next_page = reverse_lazy("inicio")


def registro(request):
    if request.method == "POST":
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada. Ahora puedes iniciar sesión.")
            return redirect("cliente_login")
    else:
        form = ClienteRegistroForm()

    return render(request, "clientes/registro.html", {"form": form})

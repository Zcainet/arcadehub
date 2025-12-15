from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistroClienteForm(UserCreationForm):
    """Formulario de registro simple para clientes."""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# ---------------------------------------------------------------------------
# Compatibilidad con el resto del proyecto
# ---------------------------------------------------------------------------
# En clientes/views.py se importan estos nombres:
#   from .forms import ClienteAuthForm, ClienteRegistroForm
# Algunas versiones del proyecto usaban RegistroClienteForm.
# Definimos aliases para evitar ImportError.


class ClienteRegistroForm(RegistroClienteForm):
    """Alias de RegistroClienteForm (mismo formulario)."""

    pass


class ClienteAuthForm(AuthenticationForm):
    """Formulario de login para clientes (alias de AuthenticationForm)."""

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )

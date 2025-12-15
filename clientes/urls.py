
from django.urls import path
from .views import registro, ClienteLoginView, ClienteLogoutView

urlpatterns = [
    path("login/", ClienteLoginView.as_view(), name="cliente_login"),
    path("logout/", ClienteLogoutView.as_view(), name="cliente_logout"),
    path("registro/", registro, name="cliente_registro"),
]

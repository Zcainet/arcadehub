from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = "ArcadeHub Admin"
admin.site.site_title = "ArcadeHub"
admin.site.index_title = "Panel de administración"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("paginas.urls")),
    path("catalogo/", include("inventario.urls")),
    path("proveedores/", include("proveedores.urls")),
    path("comunidad/", include("comunidad.urls")),
    path("cuenta/", include("clientes.urls")),
    path("sucursales/", include("tiendas.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<<<<<<< HEAD

# ArcadeHub (Game Center) — Proyecto CORREGIDO

Este ZIP corre **por defecto** en SQLite para que NO te bloquee si MySQL/MariaDB está apagado.
Si tu profe te pide MySQL en localhost, cámbialo con `USE_SQLITE=0`.

## Instalar
```bash
pip install -r requirements.txt
```

## Arrancar rápido (SQLite)
**PowerShell (Windows):**
```powershell
set USE_SQLITE=1
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Localhost con MySQL/MariaDB (XAMPP / MariaDB / MySQL)
1) Enciende MySQL (XAMPP Control Panel -> Start MySQL)
2) Crea la BD:
```sql
CREATE DATABASE arcadehub_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
3) Variables y migración:
```powershell
set USE_SQLITE=0
set MYSQL_DB=arcadehub_db
set MYSQL_USER=root
set MYSQL_PASSWORD=
set MYSQL_HOST=127.0.0.1
set MYSQL_PORT=3306
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Nota: En Windows/Python 3.13 este proyecto usa **PyMySQL** como reemplazo de `MySQLdb` automáticamente.

## PythonAnywhere (SQLite)
Variables:
- USE_SQLITE=1
- DJANGO_DEBUG=0
- DJANGO_ALLOWED_HOSTS=tuusuario.pythonanywhere.com

Luego:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```


## Funciones nuevas (upgrade)
- Login/Registro de clientes (ruta: /cuenta/)
- Solo clientes logueados pueden publicar comentarios en /comunidad/
- Reseñas y calificación de productos desde el detalle (ruta: /catalogo/p/<id>/)
- Barra de búsqueda en el encabezado (catálogo)
- Módulo de sucursales (ruta: /sucursales/) con enlace a Google Maps si hay coordenadas
=======
# arcadehub
>>>>>>> 90faaaa8a38c3b92d13de1f074edf4d036f561e2

from django.contrib import admin

# Register your models here.
from .models import Libro  # Importa el modelo creado
admin.site.register(Libro)  # Lo registra para que aparezca en el panel de admin


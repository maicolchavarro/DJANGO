from django.urls import path  # Importa el módulo para definir rutas
from . import views



urlpatterns = [
    path('', views.lista_libros, name='inicio'),  # ← esta es la raíz
]
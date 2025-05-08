from django.shortcuts import render

# Create your views here.
from .models import Libro            # Importa el modelo

def lista_libros(request):
    libros = Libro.objects.all()  # Obtiene todos los libros
    return render(request, 'catalogo/lista.html', {'libros': libros})  # Renderiza la plantilla con los datos


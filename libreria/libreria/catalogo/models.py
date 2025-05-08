from django.db import models # Importa el módulo de modelos de Django

# Define un modelo llamado Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=100)  # Campo de texto para el título
    autor = models.CharField(max_length=100)   # Campo de texto para el autor
    genero = models.CharField(max_length=50)   # Campo agregado: género del libro
    link = models.CharField(max_length=200, default='https://ejemplo.com')

    def __str__(self):
        return self.titulo  # Representación del objeto como cadena

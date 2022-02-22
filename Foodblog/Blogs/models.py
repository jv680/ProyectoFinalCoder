from django.db import models

class Recetas(models.Model):
    Nombre = (models.CharField(max_length=40))
    categoría = (models.CharField(max_length=40))
    ingredientes = (models.CharField(max_length=2000))
    preparación = (models.CharField(max_length=2000))
    
    def __str__(self) -> str:
        return f"Nombre: {self.Nombre} Ingredientes: {self.ingredientes} Preparación: {self.preparación}"      
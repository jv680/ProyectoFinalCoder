from django.db import models

class PerfilesDeUsuario(models.Model):
    usuario = (models.CharField(max_length=40))
    email = (models.CharField(max_length=40))
    Nombre = (models.CharField(max_length=40))
    Apellido = (models.CharField(max_length=40))
    Recetas = (models.CharField(max_length=2000))
    
    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"
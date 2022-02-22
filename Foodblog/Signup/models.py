from django.db import models

class User(models.Model):
    usuario = (models.CharField(max_length=40))
    email = (models.CharField(max_length=40))
    contraseña = (models.CharField(max_length=40))
    
    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"
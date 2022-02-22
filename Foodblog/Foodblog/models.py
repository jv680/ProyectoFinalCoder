from django.db import models

class User(models.Model):
    usuario2 = (models.CharField(max_length=40))
    email2 = (models.CharField(max_length=40))
    contraseña2 = (models.CharField(max_length=40))
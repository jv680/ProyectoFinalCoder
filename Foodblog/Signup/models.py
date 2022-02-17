from django.db import models

class User(models.Model):
    email = (models.CharField(max_length=40))
    password = (models.CharField(max_length=40))
    username = (models.CharField(max_length=40))
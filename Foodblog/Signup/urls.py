from django.urls import path
from Signup import views


urlpatterns = [
    path('Formulario', views.formulario, name='formulario'),
  
]
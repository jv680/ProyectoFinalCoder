from django.shortcuts import render
from Profiles.models import PerfilesDeUsuario

def profiles(request):
    
    perfiles = PerfilesDeUsuario.objects.all()
    
    contexto = {"perfiles":perfiles}
    
    return render(request, "profiles.html", contexto)
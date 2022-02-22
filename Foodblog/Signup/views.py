from django.shortcuts import render
from Signup.forms import Userdata
from Signup.models import User

def formulario(request):
    
    if request.method == 'POST':
        
        datosusuario = Userdata(request.POST)
        
        print(datosusuario)
        
        if datosusuario.is_valid:
            
            informacion = datosusuario.cleaned_data
            
            datos = User (usuario=informacion['usuario'], email=informacion['email'], contraseña=informacion['contraseña'])
       
            datos.save()
            
            return render(request, "index.html")
        
    else:
        
        datosusuario = Userdata()
    
    return render(request, "formulario.html", {"datosusuario":datosusuario})
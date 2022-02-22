from django.http import HttpResponse
from django.shortcuts import render
# from Signup.forms import Userdata
# from Signup.models import User
from django.contrib.auth.forms import UserCreationForm

# def formulario(request):
    
#     if request.method == 'POST':
        
#         datosusuario = Userdata(request.POST)
        
#         print(datosusuario)
        
#         if datosusuario.is_valid:
            
#             informacion = datosusuario.cleaned_data
            
#             datos = User (usuario=informacion['usuario'], email=informacion['email'], contraseña=informacion['contraseña'])
       
#             datos.save()
            
#             return render(request, "index.html")
        
#     else:
        
#         datosusuario = Userdata()
    
#     return render(request, "formulario.html", {"datosusuario":datosusuario})



def formulario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} creado correctamente')
            
    else:
        form = UserCreationForm()
    
    return render(request, 'formulario.html', {'form':form})
        
        
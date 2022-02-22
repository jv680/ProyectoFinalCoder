from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get('usuario')
            passw = form.cleaned_data.get('contraseña')
            
            user = authenticate(usuario=user, contraseña=passw)
            
            if user is not None:
                login(request, user)
                
                return render(request, "index.html", {"mensaje": f"Bienvenido {user}"})
            
            else:
            
                return render(request, "index.html", {"mensaje": "Error, datos incorrectos"})
        
        else:
        
            return render(request, "index.html", {"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})



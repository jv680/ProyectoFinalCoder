from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            usern = authenticate(username=user, password=passw)
            
            if usern is not None:
                login(request, usern)
                return redirect('home')
            else:
                return render(request, "loging.html", 
                    {'form': form,
                     'error': 'No es válido el usuario o la contraseña'})
            
        else:
            return render(request, 'login.html', {"form": form})
        
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



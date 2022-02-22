from django.forms import model_to_dict
from django.shortcuts import redirect, render
from Blogs.forms import AgregarReceta
from Blogs.models import Recetas

def blog(request):
    
    recetas = Recetas.objects.all()
    
    contexto = {"recetas":recetas}
    
    return render(request, "blog.html", contexto)


def addreceta(request):
    
    if request.method == 'POST':
        
        nuevareceta = AgregarReceta(request.POST)
        
        print(nuevareceta)
        
        if nuevareceta.is_valid:
            
            addreceta = nuevareceta.cleaned_data
            
            receta = Recetas (Nombre=addreceta['Nombre'], categoría=addreceta['categoría'], ingredientes=addreceta['ingredientes'], preparación=addreceta['preparación'])
       
            receta.save()
            
            return render(request, "index.html")
        
    else:
        
        nuevareceta = AgregarReceta()
    
    return render(request, "blogadd.html", {"nuevareceta":nuevareceta})


def deletereceta(request, id_receta):
    
    receta = Recetas.objects.get(id=id_receta)
    receta.delete()
    
    return redirect('blog')


def updateRecetas(request, id_receta):
    
    receta = Recetas.objects.get(id=id_receta)
        
    if request.method == 'POST':
        
        nuevareceta = AgregarReceta(request.POST)
        
        print(nuevareceta)
        
        if nuevareceta.is_valid:
            
            addreceta=nuevareceta.cleaned_data
            
            receta.Nombre = addreceta['Nombre']
            receta.categoría = addreceta['categoría']
            receta.ingredientes = addreceta['ingredientes']
            receta.preparación = addreceta['preparación']      
            
            receta.save()
            
            return redirect('blog')
        
    else:
        
        nuevareceta = AgregarReceta(model_to_dict(receta))
    
    return render(request, "blogadd.html", {"nuevareceta":nuevareceta})


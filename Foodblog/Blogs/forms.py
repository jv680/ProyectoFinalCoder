from django import forms

class AgregarReceta(forms.Form):
    
    Nombre = forms.CharField()
    categoría = forms.CharField()
    ingredientes = forms.CharField()
    preparación = forms.CharField()
    

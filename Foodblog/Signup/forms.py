from django import forms

class Userdata(forms.Form):
    
    usuario = forms.CharField()
    email = forms.EmailField()
    contraseña = forms.CharField()
    

from socket import fromshare
from django import forms

class Formulario_teclados(forms.Form):
    nombre = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=100)
    mecanico = forms.CharField(max_length=100)
    precio = forms.FloatField()
    stock = forms.IntegerField()
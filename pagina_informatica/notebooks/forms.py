from socket import fromshare
from django import forms

class Formulario_notebooks(forms.Form):
    nombre = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=100)
    procesador = forms.CharField(max_length=100)
    ram = forms.CharField(max_length=100)
    pulgadas = forms.CharField(max_length=50)
    almacenamiento = forms.CharField(max_length=50)
    precio = forms.FloatField()
    stock = forms.IntegerField()
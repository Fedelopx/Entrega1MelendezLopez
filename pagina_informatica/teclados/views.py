from http.client import HTTPResponse
from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from teclados.models import Teclados
from teclados.forms import Formulario_teclados

def crear_teclado(request):

    if request.method == 'POST':
        form = Formulario_teclados(request.POST)

        if form.is_valid():
            Teclados.objects.create(
                nombre = form.cleaned_data['nombre'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'], 
                mecanico = form.cleaned_data['mecanico'],
                precio = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(lista_teclados)

    elif request.method == 'GET':
        form = Formulario_teclados()
        context = {'form':form}
        return render(request, 'teclados/nuevo_teclado.html', context=context)


def lista_teclados(request):
    teclados = Teclados.objects.all() 
    context = {
        'teclados':teclados
    }
    return render(request, 'teclados/teclados_lista.html', context=context)

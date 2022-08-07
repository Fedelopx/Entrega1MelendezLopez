from http.client import HTTPResponse
from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from monitores.models import Monitores
from monitores.forms import Formulario_monitor

def crear_monitor(request):

    if request.method == 'POST':
        form = Formulario_monitor(request.POST)

        if form.is_valid():
            Monitores.objects.create(
                nombre = form.cleaned_data['nombre'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'], 
                pulgadas = form.cleaned_data['pulgadas'],
                precio = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(lista_monitores)

    elif request.method == 'GET':
        form = Formulario_monitor()
        context = {'form':form}
        return render(request, 'monitores/nuevo_monitor.html', context=context)


def lista_monitores(request):
    monitores = Monitores.objects.all() 
    context = {
        'monitores':monitores
    }
    return render(request, 'monitores/monitores_lista.html', context=context)

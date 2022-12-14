from django.shortcuts import render, redirect
from notebooks.models import Notebooks
from notebooks.forms import Formulario_notebooks

def crear_notebook(request):

    if request.method == 'POST':
        form = Formulario_notebooks(request.POST)

        if form.is_valid():
            Notebooks.objects.create(
                nombre = form.cleaned_data['nombre'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'], 
                procesador = form.cleaned_data['procesador'],
                ram = form.cleaned_data['ram'],
                pulgadas = form.cleaned_data['pulgadas'],
                almacenamiento = form.cleaned_data['almacenamiento'],
                precio = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(lista_notebooks)

    elif request.method == 'GET':
        form = Formulario_notebooks()
        context = {'form':form}
        return render(request, 'notebooks/nueva_notebook.html', context=context)


def lista_notebooks(request):
    notebooks = Notebooks.objects.all() 
    context = {
        'notebooks':notebooks
    }
    return render(request, 'notebooks/notebooks_lista.html', context=context)

def search_notebooks(request):
    search = request.GET['search']
    notebooks = Notebooks.objects.filter(nombre__icontains=search)
    context = {'notebooks':notebooks}
    return render(request, 'notebooks/search_notebooks.html', context=context)


def delete_notebook(request, pk):
    if request.method == 'GET':
        notebook = Notebooks.objects.get(pk=pk)
        context = {'notebook':notebook}
        return render(request, 'notebooks/delete_notebook.html', context=context)
    elif request.method == 'POST':
        notebook = Notebooks.objects.get(pk=pk)
        notebook.delete()
        return redirect(lista_notebooks)
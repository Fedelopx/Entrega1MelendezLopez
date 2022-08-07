from itertools import product
from multiprocessing import context
from django.shortcuts import render
from notebooks.models import Notebooks

def crear_notebook(request):

    nueva_notebook= Notebooks.objects.create(
        nombre= 'Notebook', 
        marca='Dell', 
        modelo='Inspiron', 
        procesador='Intel Core i7',
        ram=' 8GB',
        pulgadas='15,6',
        almacenamiento='1 TB SSD',
        precio= 100405,
        stock=20
        )
    context={
        'nueva_notebook':nueva_notebook
    }
    return render(request, 'notebooks/nueva_notebook.html', context=context)


def lista_notebooks(request):
    notebooks = Notebooks.objects.all() 
    context = {
        'notebooks':notebooks
    }
    return render(request, 'notebooks/notebooks_lista.html', context=context)


from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def saludo (request):
    return HttpResponse('Bienvenidos a todos ')

def segundo_template(request):
    context ={
        'name': 'Fede',
        'last_name': 'Melendez',
    }
    return render (request, 'template_2.html', context=context)
from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import  datetime

def saludo (request):
    return HttpResponse('Bienvenidos a todos ')
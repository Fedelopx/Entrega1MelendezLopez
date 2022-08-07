import imp
from django.contrib import admin
from django.urls import path, include
from pagina_informatica.views import saludo
from notebooks.views import crear_notebook,lista_notebooks

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/', saludo, name='saludo'),
    path('notebooks/',include('notebooks.urls'))
]
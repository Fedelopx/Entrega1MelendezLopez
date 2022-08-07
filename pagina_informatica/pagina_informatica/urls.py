import imp
from django.contrib import admin
from django.urls import path, include
from pagina_informatica.views import saludo
from notebooks.views import crear_notebook,lista_notebooks
from monitores.views import crear_monitor,lista_monitores
from teclados.views import crear_teclado,lista_teclados

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/', saludo, name='saludo'),
    path('notebooks/',include('notebooks.urls')),
    path('monitores/',include('monitores.urls')),
    path('teclados/',include('teclados.urls'))


]
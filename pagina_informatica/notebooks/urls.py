from django.urls import path
from notebooks.views import lista_notebooks,crear_notebook, busqueda_notebooks

urlpatterns = [
    path ('lista-notebooks/',lista_notebooks, name='lista_notebooks'),
    path ('crear-notebook/',crear_notebook,name='crear_notebook'),
    path('busqueda-notebooks/', busqueda_notebooks, name='busqueda_notebooks')

]
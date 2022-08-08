from django.urls import path
from notebooks.views import lista_notebooks,crear_notebook, search_notebooks

urlpatterns = [
    path ('lista-notebooks/',lista_notebooks, name='lista_notebooks'),
    path ('crear-notebook/',crear_notebook,name='crear_notebook'),
    path ('search-notebooks/',search_notebooks, name='search_notebooks')

]
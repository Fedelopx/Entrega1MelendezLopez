from django.urls import path
from notebooks.views import lista_notebooks,crear_notebook, search_notebooks,delete_notebook

urlpatterns = [
    path ('lista-notebooks/',lista_notebooks, name='lista_notebooks'),
    path ('crear-notebook/',crear_notebook,name='crear_notebook'),
    path ('search-notebooks/',search_notebooks, name='search_notebooks'),
    path ('delete-notebook/<int:pk>/',delete_notebook, name='delete_notebook')

]
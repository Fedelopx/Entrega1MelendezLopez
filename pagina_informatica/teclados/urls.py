from django.urls import path
from teclados.views import lista_teclados,crear_teclado

urlpatterns = [
    path ('lista-teclados/',lista_teclados, name='lista_teclados'),
    path ('crear-teclado/',crear_teclado,name='crear_teclado'),

]
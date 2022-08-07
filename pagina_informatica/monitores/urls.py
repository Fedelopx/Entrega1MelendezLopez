from django.urls import path
from monitores.views import lista_monitores,crear_monitor

urlpatterns = [
    path ('lista-monitores/',lista_monitores, name='lista_monitores'),
    path ('crear-monitor/',crear_monitor,name='crear_monitor'),
]
from django.contrib import admin
from teclados.models import Teclados

@admin.register(Teclados)
class teclados_admin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'modelo', 'mecanico', 'precio', 'is_active', 'stock']

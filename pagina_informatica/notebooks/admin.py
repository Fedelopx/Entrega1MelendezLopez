from django.contrib import admin
from notebooks.models import Notebooks

@admin.register(Notebooks)
class notebooks_admin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'modelo', 'procesador', 'ram', 'pulgadas', 'almacenamiento', 'precio', 'is_active', 'stock']
    

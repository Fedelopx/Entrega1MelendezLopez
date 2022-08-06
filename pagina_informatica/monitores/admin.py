from django.contrib import admin
from monitores.models import Monitores

@admin.register(Monitores)
class monitores_admin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'modelo', 'pulgadas', 'precio', 'is_active', 'stock']
    

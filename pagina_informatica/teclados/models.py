from django.db import models

class Teclados (models.Model): 
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    mecanico = models.CharField(max_length=50)
    precio = models.FloatField()
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()

    def __str__(self): 
        return self.nombre

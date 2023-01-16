from django.db import models


class Cliente(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    dias = models.CharField(max_length=60)
    longitud = models.FloatField()
    latitud = models.FloatField()
    tipo = models.CharField(max_length=20)
    sector = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
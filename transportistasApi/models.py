from django.db import models


class Transportista(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
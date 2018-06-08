from django.db import models


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año_fabricacion = models.CharField(max_length=4, blank=True, null=True)
    es_aire_acondicionado = models.BooleanField(),
    capacidad_btu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_equipo'

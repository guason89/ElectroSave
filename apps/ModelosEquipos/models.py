from django.db import models
from apps.Modelos.models import ProveedorModelos
#from apps.TipoEquipo.models import TipoEquipo
class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)
        
    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

    def __str__ ( self ):
        return self.tipo_equipo


class ModeloEquipo(models.Model):
    id_modelo = models.AutoField(primary_key=True)        
    marca = models.CharField(max_length=100)
    nombre_modelo = models.CharField(max_length=100)
    año_fabricacion = models.CharField(max_length=4)    
    capacidad_btu = models.IntegerField(blank=True, null=True, default = 0)
    tipo = models.ForeignKey('TipoEquipo', on_delete=models.CASCADE, db_column='id_tipo_equipo')

    class Meta:
        managed = False
        db_table = 'tbl_modelo_equipo'

    def __str__ ( self ):
        return self.nombre_modelo

    def get_proveedores_asociados(self):
        prov_asoc = ProveedorModelos.objects.filter(id_modelo = self.id_modelo)
        return prov_asoc

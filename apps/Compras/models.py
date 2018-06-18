from django.db import models
from django.utils import timezone #para la fecha local

# Create your models here.
from apps.Proveedores.models import Proveedor

class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_proveedor = models.IntegerField(blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    tipo_contratacion = models.IntegerField(blank=True, null=True)
    total_compra = models.FloatField(blank=True, null=True)
    descripcion_compra = models.CharField(max_length=250, blank=True, null=True)

    
    class Meta:
        managed = False
        db_table = 'tbl_hed_compras'

    #def __str__ ( self ):
    #return self.id_compra
    
    def getProveedor(self):
        proveedor = Proveedor.objects.get(id_proveedor=self.id_proveedor) 
        return proveedor.nombre
class TblTipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

class TblModeloEquipo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_tipo_equipo = models.ForeignKey('TblTipoEquipo', models.DO_NOTHING, db_column='id_tipo_equipo')
    marca = models.CharField(max_length=100)
    nombre_modelo = models.CharField(max_length=100)
    año_fabricacion = models.CharField(max_length=4)
    es_aire_acondicionado = models.BooleanField()
    capacidad_btu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_modelo_equipo'

class TblDetCompras(models.Model):
    corr_compra = models.AutoField(primary_key=True)
    id_compra = models.IntegerField(blank=True, null=False)
    id_modelo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    valor_unidad = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    serie_equipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_det_compras'

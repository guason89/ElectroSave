from django.db import models
from django.utils import timezone #para la fecha local

# Create your models here.
class Instituciones(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    fecha_creacion_inst = models.DateField(default=timezone.now)
    nombre_inst = models.CharField(max_length=250)
    nit_inst = models.CharField(max_length=17, blank=True, null=True)
    telefono_1_inst = models.CharField(max_length=12, blank=True, null=True)
    telefono_2_inst = models.CharField(max_length=12, blank=True, null=True)
    departamento_inst = models.CharField(max_length=60, blank=True, null=True)
    municipio_inst = models.CharField(max_length=60, blank=True, null=True)
    complemento_dir = models.CharField(max_length=250, blank=True, null=True)
    presupuesto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_instituciones'

    def __str__ ( self ):
        return self.nombre_inst

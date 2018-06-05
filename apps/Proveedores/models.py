from django.db import models
from django.urls import reverse
from django.utils import timezone #para la fecha local
    
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    nit = models.CharField(max_length=17)
    fecha_alta_proveedor = models.DateField(default=timezone.now)
    telefono_1 = models.CharField(max_length=20)
    telefono_2 = models.CharField(max_length=20, blank=True, null=True)    
    email = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_proveedores'

    def __str__ ( self ):
        return self.nombre


       



 
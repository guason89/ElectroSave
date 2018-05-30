from django.db import models
from django.urls import reverse
    
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    nit = models.CharField(max_length=17)
    fecha_alta_proveedor = models.DateField()
    telefono_1 = models.CharField(max_length=20)
    telefono_2 = models.CharField(max_length=20, blank=True, null=True)
    permiso_instalacion = models.CharField(max_length=1)
    email = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_proveedores'

    def __str__ ( self ):
        return self.nombre

    def get_detalle_url(self):
        return reverse('proveedores.detalles',kwargs={'pk':self.id_proveedor})

   




 
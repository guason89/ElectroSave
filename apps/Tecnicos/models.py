from django.db import models

from apps.Proveedores.models import Proveedor

# Create your models here.

class Tecnico(models.Model):
    tecnico_id = models.AutoField(primary_key=True)        
    tecnico_nombre = models.CharField(max_length=50)    
    id_proveedor = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tbl_tecnico'
    def get_proveedor(self):
    	proveedor = Proveedor.objects.get(id_proveedor=self.id_proveedor)
    	return proveedor.nombre
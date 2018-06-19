from django.db import models

from apps.Proveedores.models import Proveedor
from apps.Tecnicos.models import Tecnico

from django.utils import timezone

class Mantenimiento(models.Model):
	mtto_id = models.AutoField(primary_key=True)
	mtto_fecha = models.DateField(default=timezone.now)
	mtto_fecha_prox = models.DateField(default=timezone.now)
	mtto_estado_i = models.CharField(max_length=25)
	mtto_estado_f = models.CharField(max_length=25)
	mtto_comentario = models.CharField(max_length=500,blank=True, null=True)
	mtto_costo = models.FloatField(blank=True, null=True)
	tecnico_id = models.IntegerField()
	equipo_id = models.CharField(max_length=10)
	class Meta:
		managed = False
		db_table = 'tbl_mantenimiento'
	def get_tecnico(self):
		tecnico = Tecnico.objects.get(tecnico_id = self.tecnico_id)
		return tecnico.tecnico_nombre
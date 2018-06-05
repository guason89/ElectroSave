from django.db import models

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

from django.db import models
from apps.ModelosEquipos.models import ModeloEquipo

from django.db import connection
from collections import namedtuple

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

    def __str__ ( self ):
        return self.tipo_equipo

    '''def equipos(self):
    	equipos = ModeloEquipo.objects.filter(nombre_modelo = 'modelo 02')
    	return equipos'''

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def getEquipos(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_modelo_equipo WHERE id_tipo_equipo = %s", [self.id_tipo_equipo])
            results = TipoEquipo.dictfetchall(cursor)      
            return results


        
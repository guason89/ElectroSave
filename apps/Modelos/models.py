from django.db import models

#para usar procedimientos o consultas directas
from django.db import connection
from collections import namedtuple

from django.utils import timezone

class Aux(models.Model):

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'

        #consulta a una funcion en postgresql
    def getPermisos(self):
        with connection.cursor() as cursor:
            cursor.callproc('f_get_permisos', [self.id])
            results =  Aux.dictfetchall(cursor) 
            return results


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default = False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'auth_user'

    def getRol(self):
        '''with connection.cursor() as cursor:
            cursor.execute('SELECT ag.id, ag.name from auth_group ag inner join auth_user_groups aug on ag.id = aug.user_id where aug.user_id = %s', [self.id])
            results =  Aux.dictfetchall(cursor) 
            return results[0]'''
        rol_user = AuthUserGroups.objects.get(user_id=self.id)
        return rol_user

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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

class ProveedorModelos(models.Model):
    id_proveedor = models.IntegerField()
    id_modelo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_proveedor_modelos'

#modelo instituciones
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

    def get_proveedores_asoc(self):
        prov_asoc = InstitucionProveedores.objects.filter(id_institucion = self.id_institucion)       
        return prov_asoc

    def getEquipos(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from v_det_equipo where id_institucion =  %s and estado_e = %s', [self.id_institucion, 'INGRESADO'])
            results =  Aux.dictfetchall(cursor) 
            return results

    def get_prov_asoc(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT pr.* from tbl_institucion_proveedores ip inner join tbl_proveedores pr on ip.id_proveedor = pr.id_proveedor where ip.id_institucion = %s', [self.id_institucion])
            results =  Aux.dictfetchall(cursor) 
            return results

#modelo hed compras
class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_proveedor = models.IntegerField()
    id_institucion = models.IntegerField()
    fecha_compra = models.DateField()
    id_tipo_cont = models.IntegerField()
    total_compra = models.FloatField(blank=True, null=True)
    descripcion_compra = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_hed_compras'

    def getProveedor(self):
        proveedor = Proveedor.objects.get(id_proveedor=self.id_proveedor) 
        return proveedor.nombre

    def getFormaContratacion(self):
        forma = FormaContratacion.objects.get(id_forma_cont=self.id_tipo_cont) 
        return forma.descripcion_tc

    def getInstitucion(self):
        institucion = Instituciones.objects.get(id_institucion=self.id_institucion) 
        return institucion.nombre_inst

    def getModelosEquipos(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT me.* from tbl_proveedor_modelos pm inner join tbl_modelo_equipo me on pm.id_modelo = me.id_modelo where pm.id_proveedor =  %s', [self.id_proveedor])
            results =  Aux.dictfetchall(cursor) 
            return results

    def getDetalles(self):
        '''detalles = DetCompras.objects.filter(id_compra = self.id_compra)
        return detalles'''
        with connection.cursor() as cursor:
            cursor.execute("SELECT cp.id_compra,cp.id_modelo||'||'||cp.cantidad||'||'||cp.valor_unidad as concatenado,cp.cantidad, cp.valor_unidad, cp.total_item, me.nombre_modelo from tbl_det_compras cp inner join tbl_modelo_equipo me on cp.id_modelo = me.id_modelo where id_compra =  %s", [self.id_compra])
            results =  Aux.dictfetchall(cursor) 
            return results

#modelo  forma contratacion
class FormaContratacion(models.Model):
    id_forma_cont = models.AutoField(primary_key=True)
    descripcion_tc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_forma_contratacion'

#modelo detalle compra
class DetCompras(models.Model):
    id_detalle_compra = models.AutoField(primary_key=True)
    id_compra = models.IntegerField()
    id_modelo = models.IntegerField()
    cantidad = models.IntegerField(blank=True, null=True)
    valor_unidad = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    total_item = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_det_compras'

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)
        
    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

    def __str__ ( self ):
        return self.tipo_equipo

#modelo modelo equipo
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

#modelo institucion proveedores
class InstitucionProveedores(models.Model):
    id_institucion = models.IntegerField()
    id_proveedor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_institucion_proveedores'

#modelo equipos
class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    num_serie_e = models.CharField(max_length=60, blank=True, null=True)
    id_modelo = models.IntegerField()
    id_institucion = models.IntegerField()
    id_detalle_compra = models.IntegerField()
    estado_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_equipos'

#modelo instalaciones
class Instalacion(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    id_proveedor = models.IntegerField()
    fecha_inst = models.DateField(blank=True, null=True)
    fecha_sol_inst = models.DateField(default=timezone.now)
    estatus_inst = models.CharField(max_length=20, blank=True, null=True)
    id_equipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_instalacion'
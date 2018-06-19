# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


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


class TblDetCompras(models.Model):
    id_detalle_compra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey('TblHedCompras', models.DO_NOTHING, db_column='id_compra')
    id_modelo = models.ForeignKey('TblModeloEquipo', models.DO_NOTHING, db_column='id_modelo')
    cantidad = models.IntegerField(blank=True, null=True)
    valor_unidad = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    total_item = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_det_compras'


class TblEquipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    num_serie_e = models.CharField(max_length=60, blank=True, null=True)
    id_modelo = models.ForeignKey('TblModeloEquipo', models.DO_NOTHING, db_column='id_modelo', blank=True, null=True)
    id_institucion = models.ForeignKey('TblInstituciones', models.DO_NOTHING, db_column='id_institucion', blank=True, null=True)
    id_detalle_compra = models.IntegerField()
    estado_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_equipos'


class TblFormaContratacion(models.Model):
    id_forma_cont = models.AutoField(primary_key=True)
    descripcion_tc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_forma_contratacion'


class TblHedCompras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey('TblProveedores', models.DO_NOTHING, db_column='id_proveedor')
    id_institucion = models.ForeignKey('TblInstituciones', models.DO_NOTHING, db_column='id_institucion')
    fecha_compra = models.DateField()
    id_tipo_cont = models.ForeignKey(TblFormaContratacion, models.DO_NOTHING, db_column='id_tipo_cont')
    total_compra = models.FloatField(blank=True, null=True)
    descripcion_compra = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_hed_compras'


class TblInstalacion(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey('TblProveedores', models.DO_NOTHING, db_column='id_proveedor')
    fecha_inst = models.DateField(blank=True, null=True)
    fecha_sol_inst = models.DateField(blank=True, null=True)
    estatus_inst = models.CharField(max_length=-1, blank=True, null=True)
    id_equipo = models.ForeignKey(TblEquipos, models.DO_NOTHING, db_column='id_equipo')

    class Meta:
        managed = False
        db_table = 'tbl_instalacion'


class TblInstitucionProveedores(models.Model):
    id_institucion = models.ForeignKey('TblInstituciones', models.DO_NOTHING, db_column='id_institucion')
    id_proveedor = models.ForeignKey('TblProveedores', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'tbl_institucion_proveedores'


class TblInstituciones(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    fecha_creacion_inst = models.DateField()
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


class TblIntentos(models.Model):
    id_intento = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    intentos = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_intentos'


class TblModeloEquipo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_tipo_equipo = models.ForeignKey('TblTipoEquipo', models.DO_NOTHING, db_column='id_tipo_equipo')
    marca = models.CharField(max_length=100)
    nombre_modelo = models.CharField(max_length=100)
    año_fabricacion = models.CharField(max_length=4)
    capacidad_btu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_modelo_equipo'


class TblProveedorModelos(models.Model):
    id_proveedor = models.ForeignKey('TblProveedores', models.DO_NOTHING, db_column='id_proveedor')
    id_modelo = models.ForeignKey(TblModeloEquipo, models.DO_NOTHING, db_column='id_modelo')

    class Meta:
        managed = False
        db_table = 'tbl_proveedor_modelos'


class TblProveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    nit = models.CharField(max_length=17)
    fecha_alta_proveedor = models.DateField()
    telefono_1 = models.CharField(max_length=20)
    telefono_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_proveedores'


class TblTipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    tipo_equipo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tbl_tipo_equipo'

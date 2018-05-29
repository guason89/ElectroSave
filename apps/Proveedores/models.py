from django.db import models

class ContactoProveedor(models.Model):
    id_contacto_proveedor = models.AutoField(primary_key=True)
    id_proveedor = models.IntegerField()
    nombre_contacto = models.CharField(max_length=250)
    telefono1_contacto = models.CharField(max_length=30)
    telefono2_contacto = models.CharField(max_length=30, blank=True, null=True)
    email_contacto = models.CharField(max_length=50, blank=True, null=True)
    dui_contacto = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_contactos_proveedores'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    id_contacto_proveedor = models.IntegerField(blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=250)
    direccion_proveedor = models.CharField(max_length=250)
    nit_proveedor = models.CharField(max_length=15)
    fecha_alta_proveedor = models.DateField(blank=True, null=True)
    telefono_proveedor = models.CharField(max_length=30)
    permiso_instalacion = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_proveedores'


   




 
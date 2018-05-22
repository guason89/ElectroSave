from django.contrib import admin

# Register your models here.
from apps.Proveedores import models
admin.site.register(models.Proveedor)

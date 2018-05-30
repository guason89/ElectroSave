from django.urls import path

from apps.Proveedores import views


urlpatterns = [
    path ( '' , views.ProveedorList.as_view() , name = 'proveedores.index' ),
    path ( 'nuevo' , views.ProveedorCreate.as_view() , name = 'proveedores.nuevo' ),
    path ( 'actualizar/<pk>' , views.ProveedorActualizar.as_view() , name = 'proveedores.actualizar' ),  
    path ( 'detalle/<pk>' , views.ProveedorDetalles.as_view() , name = 'proveedores.detalles' ),  
    path ( 'eliminar/<pk>' , views.ProveedorEliminar.as_view() , name = 'proveedores.eliminar' ),
]

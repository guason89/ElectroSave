from django.urls import path

from apps.Proveedores.views import ProveedorList,ProveedorCreate,ProveedorActualizar,ProveedorDetalles,ProveedorEliminar




urlpatterns = [
    path ( '' , ProveedorList.as_view() , name = 'proveedores.index' ),
    path ( 'nuevo' , ProveedorCreate.as_view() , name = 'proveedores.nuevo' ),
    path ( 'actualizar/<pk>' , ProveedorActualizar.as_view() , name = 'proveedores.actualizar' ),  
    path ( 'detalle/<pk>' , ProveedorDetalles.as_view() , name = 'proveedores.detalles' ),  
    path ( 'eliminar/<pk>' , ProveedorEliminar.as_view() , name = 'proveedores.eliminar' ),
]

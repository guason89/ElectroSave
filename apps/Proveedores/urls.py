from django.urls import path

from apps.Proveedores.views import ProveedorList,ProveedorCreate,ProveedorActualizar,ProveedorDetalles,ProveedorEliminar

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(ProveedorList.as_view()) , name = 'proveedores.index' ),
    path ( 'nuevo' , login_required(ProveedorCreate.as_view()) , name = 'proveedores.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(ProveedorActualizar.as_view()) , name = 'proveedores.actualizar' ),  
    path ( 'detalle/<pk>' , login_required(ProveedorDetalles.as_view()) , name = 'proveedores.detalles' ),  
    path ( 'eliminar/<pk>' , login_required(ProveedorEliminar.as_view()) , name = 'proveedores.eliminar' ),
]

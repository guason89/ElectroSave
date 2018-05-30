from django.urls import path

from apps.Proveedores import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(views.ProveedorList.as_view()) , name = 'proveedores.index' ),
    path ( 'nuevo' , login_required(views.ProveedorCreate.as_view()) , name = 'proveedores.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(views.ProveedorActualizar.as_view()) , name = 'proveedores.actualizar' ),  
    path ( 'detalle/<pk>' , login_required(views.ProveedorDetalles.as_view()) , name = 'proveedores.detalles' ),  
    path ( 'eliminar/<pk>' , login_required(views.ProveedorEliminar.as_view()) , name = 'proveedores.eliminar' ),
]

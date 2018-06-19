from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Compras.views import comprasList,comprasCreate, comprasActualizar, ComprasDetalles
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path( '' , login_required(comprasList.as_view()) , name = 'compras.index' ),
    path( 'nuevo' , login_required(comprasCreate.as_view()) , name = 'compras.nuevo' ),
    path( 'actualizar/<pk>' , login_required(comprasActualizar.as_view()) , name = 'compras.actualizar' ),  
    path( 'detalle/<pk>' , login_required(ComprasDetalles.as_view()) , name = 'compras.detalles' ),  
    #path ( 'eliminar/<pk>' , InstitucionesEliminar.as_view() , name = 'instituciones.eliminar' ),
]
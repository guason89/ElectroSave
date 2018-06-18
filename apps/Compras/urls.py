from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Compras.views import comprasList,comprasCreate, comprasActualizar
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(comprasList.as_view()) , name = 'compras.index' ),
    path ( 'nuevo' , login_required(comprasCreate.as_view()) , name = 'compras.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(comprasActualizar.as_view()) , name = 'compras.actualizar' ),  
    #path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    #path ( 'eliminar/<pk>' , InstitucionesEliminar.as_view() , name = 'instituciones.eliminar' ),
]
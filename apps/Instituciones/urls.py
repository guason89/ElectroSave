from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Instituciones.views import InstitucionesList, InstitucionesCreate,InstitucionesActualizar
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(InstitucionesList.as_view()) , name = 'instituciones.index' ),
    path ( 'nuevo' , login_required(InstitucionesCreate.as_view()) , name = 'instituciones.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(InstitucionesActualizar.as_view()) , name = 'instituciones.actualizar' ),  
    #path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    path ( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'tipo_equipo.eliminar' ),
]
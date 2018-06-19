from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Instituciones.views import InstitucionesList, InstitucionesCreate,InstitucionesActualizar,InstitucionesEliminar
from django.contrib.auth.decorators import login_required

from apps.Instituciones.views import InstitucionInstalacion


urlpatterns = [
    path ( '' , login_required(InstitucionesList.as_view()) , name = 'instituciones.index' ),
    path ( 'nuevo' , login_required(InstitucionesCreate.as_view()) , name = 'instituciones.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(InstitucionesActualizar.as_view()) , name = 'instituciones.actualizar' ),     
    path ( 'eliminar/<pk>' , login_required(InstitucionesEliminar.as_view()) , name = 'instituciones.eliminar' ),
    path ( 'programar/instalacion/<pk>' , login_required(InstitucionInstalacion.as_view()) , name = 'instituciones.instalacion' ), 
]
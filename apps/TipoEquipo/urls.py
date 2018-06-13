from django.urls import path

from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, TipoEquipoEliminar

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(TipoEquipoList.as_view()) , name = 'tipo_equipo.index' ),
    path ( 'nuevo' , login_required(TipoEquipoCreate.as_view()) , name = 'tipo_equipo.nuevo' ),
    path ( 'actualizar/<pk>' , TipoEquipoActualizar.as_view() , name = 'tipo_equipo.actualizar' ),  
    path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    path ( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'tipo_equipo.eliminar' ),
]
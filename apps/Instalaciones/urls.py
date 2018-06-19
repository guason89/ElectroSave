from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Instalaciones.views import InstalacionesList, InstalacionesActualizar
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path( '' , login_required(InstalacionesList.as_view()) , name = 'instalaciones.index' ),
    path('actualizar/<pk>' , login_required(InstalacionesActualizar.as_view()) , name = 'instalaciones.actualizar' ), 
]
'''path ( 'nuevo' , login_required(InstitucionesCreate.as_view()) , name = 'instalaciones.nuevo' ),
     
    #path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    path ( 'eliminar/<pk>' , InstitucionesEliminar.as_view() , name = 'instalaciones.eliminar' ),'''
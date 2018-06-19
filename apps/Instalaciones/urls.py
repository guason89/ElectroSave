from django.urls import path

'''from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate, TipoEquipoActualizar, TipoEquipoDetalles, \
TipoEquipoEliminar'''
from apps.Instalaciones.views import InstalacionesList
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(InstalacionesList.as_view()) , name = 'instalaciones.index' ),
    
]
'''path ( 'nuevo' , login_required(InstitucionesCreate.as_view()) , name = 'instalaciones.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(InstitucionesActualizar.as_view()) , name = 'instalaciones.actualizar' ),  
    #path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    path ( 'eliminar/<pk>' , InstitucionesEliminar.as_view() , name = 'instalaciones.eliminar' ),'''
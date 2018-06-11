from django.urls import path

from apps.Roles.views import RolesList, RolesUpdate

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('' , login_required(RolesList.as_view()) , name = 'roles.index' ),
    
    path('actualizar/<pk>' , login_required(RolesUpdate.as_view()) , name = 'roles.actualizar' ),  
    
]

'''path ( 'nuevo' , login_required(TipoEquipoCreate.as_view()) , name = 'tipo_equipo.nuevo' ),
path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'tipo_equipo.detalles' ),  
    path ( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'tipo_equipo.eliminar' ),'''
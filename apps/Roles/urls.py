from django.urls import path

from apps.Roles.views import RolesList, RolesCreate, RolesUpdate, RolesDelete

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('' , login_required(RolesList.as_view()) , name = 'roles.index' ),
    path( 'nuevo' , login_required(RolesCreate.as_view()) , name = 'roles.nuevo' ),
    path('actualizar/<pk>' , login_required(RolesUpdate.as_view()) , name = 'roles.actualizar' ),  
    path('eliminar/<pk>', login_required(RolesDelete.as_view()) , name = 'roles.eliminar' )
]

'''path ( 'nuevo' , login_required(TipoEquipoCreate.as_view()) , name = 'tipo_equipo.nuevo' ),
,  
    path ( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'tipo_equipo.eliminar' ),'''
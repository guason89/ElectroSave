from django.urls import path

from apps.Usuarios.views import UsuarioList

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(UsuarioList.as_view()) , name = 'usuarios.index' ),
    
]


'''path ( 'nuevo' , login_required(TipoEquipoCreate.as_view()) , name = 'usuarios.nuevo' ),
    path ( 'actualizar/<pk>' , TipoEquipoActualizar.as_view() , name = 'usuarios.actualizar' ),  
    path ( 'detalle/<pk>' , TipoEquipoDetalles.as_view() , name = 'usuarios.detalles' ),  
    path ( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'usuarios.eliminar' ),'''
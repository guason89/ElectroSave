from django.urls import path

from apps.Usuarios.views import UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDetalles, SendEmail,SendEmailInterno

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path( '' , login_required(UsuarioList.as_view()) , name = 'usuarios.index' ),
    path( 'nuevo' , login_required(UsuarioCreate.as_view()) , name = 'usuarios.nuevo' ),
    path( 'actualizar/<pk>' , login_required(UsuarioUpdate.as_view()) , name = 'usuarios.actualizar' ),
    path( 'detalle/<pk>' , login_required(UsuarioDetalles.as_view()) , name = 'usuarios.detalles' ),

    path( 'sendMail' , SendEmail.as_view(), name = 'usuarios.sendemail' ),
    path( 'solicitar' , login_required(SendEmailInterno.as_view()), name = 'usuarios.sendemailinterno' )
]


'''
    path( 'actualizar/<pk>' , TipoEquipoActualizar.as_view() , name = 'usuarios.actualizar' ),     
    path( 'eliminar/<pk>' , TipoEquipoEliminar.as_view() , name = 'usuarios.eliminar' ),'''
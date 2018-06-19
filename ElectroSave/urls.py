
from django.conf.urls import url

from django.contrib import admin
from django.urls import path , include
from apps.Inicio.views import Home
#from django.contrib.auth.views import login, logout_then_login
#from django.contrib.auth.decorators import login_required

from apps.Inicio.views import LogueoView , LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', Home, name  = 'home'),
    #url(r'^$', login,{'template_name':'login.html'}, name='login'),
    url(r'^$', LogueoView, name='login'),    
    url(r'^logout/$', LogoutView, name='salir'), 

    #incluir rutas de cada aplicacion
    path ( 'proveedores/' , include ( 'apps.Proveedores.urls' )),
    path ( 'tipo/equipo/' , include ( 'apps.TipoEquipo.urls' )),
    path ( 'instituciones/' , include ( 'apps.Instituciones.urls' )),
    path ( 'modelos/' , include ( 'apps.ModelosEquipos.urls' )),
    path ( 'roles/' , include ( 'apps.Roles.urls' )), 
    path ( 'usuarios/' , include ( 'apps.Usuarios.urls' )), 
    #Marvin Segura
    path ( 'mantenimientos/' , include ( 'apps.Mantenimientos.urls' )),
    path ( 'tecnicos/' , include ( 'apps.Tecnicos.urls' )),
]

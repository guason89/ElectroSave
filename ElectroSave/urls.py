
from django.conf.urls import url

from django.contrib import admin
from django.urls import path , include
from apps.Inicio.views import Home
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', login_required(Home), name  = 'home'),
    url(r'^$', login,{'template_name':'login.html'}, name='login'),
    path('accounts/login/', login,{'template_name':'login.html'}, name='login'),
    path('logout', logout_then_login, name='salir'), 

    #incluir rutas de cada aplicacion
    path ( 'proveedores/' , include ( 'apps.Proveedores.urls' )),   
]

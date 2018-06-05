from django.urls import path

from apps.TipoEquipo.views import TipoEquipoList,TipoEquipoCreate

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(TipoEquipoList.as_view()) , name = 'tipo_equipo.index' ),
    path ( 'nuevo' , login_required(TipoEquipoCreate.as_view()) , name = 'tipo_equipo.nuevo' ),
    
]
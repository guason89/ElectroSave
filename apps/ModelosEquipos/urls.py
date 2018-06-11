from django.urls import path
from django.contrib.auth.decorators import login_required

from django.urls import path

from apps.ModelosEquipos.views import ModeloList, ModeloCreate, ModeloUpdate, ModeloEquipoEliminar

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path ( '' , login_required(ModeloList.as_view()) , name = 'modelos.index' ),
    path ( 'nuevo' , login_required(ModeloCreate.as_view()) , name = 'modelos.nuevo' ),
    path ( 'actualizar/<pk>' , login_required(ModeloUpdate.as_view()) , name = 'modelos.actualizar' ), 
    path ( 'eliminar/<pk>' , login_required(ModeloEquipoEliminar.as_view()) , name = 'modelos.eliminar' )   
]
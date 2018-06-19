from django.urls import path

from apps.Tecnicos.views import TecList, TecCreate, TecActualizar, TecEliminar

urlpatterns = [
    path ( '' , TecList.as_view() , name = 'tec.index' ),
    path ( 'nuevo' , TecCreate.as_view() , name = 'tec.create' ),
    path ( 'actualizar/<pk>' , TecActualizar.as_view() , name = 'tec.update' ),
    path ( 'eliminar/<pk>' , TecEliminar.as_view() , name = 'tec.delete' ),
]
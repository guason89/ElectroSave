from django.urls import path

from apps.Mantenimientos.views import MttoList, MttoCreate, MttoActualizar, MttoEliminar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ( '' , MttoList.as_view() , name = 'mtto.index' ),
    path ( 'nuevo' , MttoCreate.as_view() , name = 'mtto.create' ),
    path ( 'actualizar/<pk>' , MttoActualizar.as_view() , name = 'mtto.update' ),
    path ( 'eliminar/<pk>' , MttoEliminar.as_view() , name = 'mtto.delete' ),
]
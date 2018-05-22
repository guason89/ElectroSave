from django.urls import path

from apps.Proveedores import views


urlpatterns = [
    path ( '' , views.ProveedorList.as_view() , name = 'proveedores.index' ),
    path ( 'nuevo' , views.ProveedorCreate.as_view() , name = 'proveedores.nuevo' ),   
]
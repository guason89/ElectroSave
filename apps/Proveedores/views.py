from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from apps.Proveedores import models
from apps.Proveedores.forms import ProveedorForm

def index ( request ):
    return render(request,'proveedores/index.html')


class ProveedorList (ListView):
	model = models.Proveedor
	template_name = 'proveedores/index.html'

class ProveedorCreate (CreateView):
	model = models.Proveedor
	form_class = ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	success_url = '/proveedores'



from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from apps.Proveedores.models import Proveedor
from apps.Proveedores import forms
from django.urls import reverse



class ProveedorList (ListView):
	model = Proveedor
	template_name = 'proveedores/index.html'

class ProveedorCreate(CreateView):
	model = Proveedor
	form_class = forms.ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	
	def get_success_url(self):
		return reverse('proveedores.index')

class ProveedorActualizar(UpdateView):
	model = Proveedor
	form_class = forms.ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	
	def get_success_url(self):
		return reverse('proveedores.index')

class ProveedorDetalles(DetailView):
	model = Proveedor
	template_name = 'proveedores/detalle.html'

class ProveedorEliminar(DeleteView):
	model = Proveedor
	template_name = 'proveedores/eliminar.html'
	def get_success_url(self):
		return reverse('proveedores.index')



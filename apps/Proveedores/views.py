from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from apps.Proveedores.models import Proveedor
from apps.Proveedores import forms
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator



class ProveedorList(LoginRequiredMixin, ListView):
	model = Proveedor
	template_name = 'proveedores/index.html'

	#@method_decorator(permission_required('Proveedores.select_proveedor',reverse_lazy('home')))
	#def dispatch(self, *args, **kwargs):
		#return super().dispatch(*args, **kwargs)

class ProveedorCreate(LoginRequiredMixin, CreateView):
	model = Proveedor
	form_class = forms.ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	
	def get_success_url(self):
		return reverse('proveedores.index')

	@method_decorator(permission_required('Proveedores.add_proveedor',reverse_lazy('home')))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class ProveedorActualizar(LoginRequiredMixin, UpdateView):
	model = Proveedor
	form_class = forms.ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	
	def get_success_url(self):
		return reverse('proveedores.index')

class ProveedorDetalles(LoginRequiredMixin, DetailView):
	model = Proveedor
	template_name = 'proveedores/detalle.html'

class ProveedorEliminar(LoginRequiredMixin, DeleteView):
	model = Proveedor
	template_name = 'proveedores/eliminar.html'
	def get_success_url(self):
		return reverse('proveedores.index')

	





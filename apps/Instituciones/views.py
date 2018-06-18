from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Instituciones.forms import InstitucionForm
from django.urls import reverse, reverse_lazy

from apps.Instituciones.models import Instituciones

class InstitucionesList (ListView):
	model = Instituciones
	template_name = 'Instituciones/index.html'

class InstitucionesCreate(CreateView):
	model = Instituciones
	form_class = InstitucionForm
	template_name = 'Instituciones/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('instituciones.index')

class InstitucionesActualizar(UpdateView):
	model = Instituciones
	form_class = InstitucionForm
	template_name = 'Instituciones/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('instituciones.index')

'''class TipoEquipoDetalles(DetailView):
	model = Instituciones
	template_name = 'Instituciones/detalle.html' '''

class InstitucionesEliminar(DeleteView):
	model = Instituciones
	template_name = 'Instituciones/eliminar.html'
	def get_success_url(self):
		return reverse_lazy('instituciones.index')
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Roles.forms import RolesForm
from django.urls import reverse, reverse_lazy

from apps.Modelos.models import AuthGroup

class RolesList (ListView):
	model = AuthGroup
	template_name = 'Roles/index.html'

'''class RolesCreate(CreateView):
	model = AuthGroup
	form_class = RolesForm
	template_name = 'TipoEquipo/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('tipo_equipo.index')'''

class RolesUpdate(UpdateView):
	model = AuthGroup
	form_class = RolesForm
	template_name = 'Roles/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('roles.index')

'''class TipoEquipoDetalles(DetailView):
	model = TipoEquipo
	template_name = 'TipoEquipo/detalle.html'

class TipoEquipoEliminar(DeleteView):
	model = TipoEquipo
	template_name = 'TipoEquipo/eliminar.html'
	def get_success_url(self):
		return reverse_lazy('tipo_equipo.index')'''
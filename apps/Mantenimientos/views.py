from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.Mantenimientos import forms
from apps.Mantenimientos.models import Mantenimiento
from apps.Mantenimientos.forms import MantenimientoForm
# Create your views here.

class MttoList(ListView):
	model = Mantenimiento
	template_name = 'Mantenimientos/index.html'

class MttoCreate(CreateView): 
	model = Mantenimiento
	form_class = forms.MantenimientoForm
	template_name = 'Mantenimientos/nuevo.html'
	def get_success_url(self):
		return reverse('mtto.index')

class MttoActualizar(UpdateView):
	model = Mantenimiento
	form_class = forms.MantenimientoForm
	template_name = 'Mantenimientos/nuevo.html'
	def get_success_url(self):
		return reverse_lazy('mtto.index')

class MttoEliminar(DeleteView):
	model = Mantenimiento
	template_name = 'Mantenimientos/eliminar.html'
	def get_success_url(self):
		return reverse('mtto.index')
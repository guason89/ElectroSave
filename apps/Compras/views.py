from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Compras.forms import ComprasForm
from django.urls import reverse, reverse_lazy

from apps.Compras.models import Compras

class comprasList(ListView):
	model = Compras
	template_name = 'compras/index.html'

class comprasCreate(CreateView):
	model = Compras
	form_class = ComprasForm
	template_name = 'compras/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('compras.index')

class comprasActualizar(UpdateView):
	model = Compras
	form_class = ComprasForm
	template_name = 'compras/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('compras.index')

'''class TipoEquipoDetalles(DetailView):
	model = compras
	template_name = 'compras/detalle.html' 

class comprasEliminar(DeleteView):
	model = compras
	template_name = 'compras/eliminar.html'
	def get_success_url(self):
		return reverse_lazy('instituciones.index')'''
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.Tecnicos import forms
from apps.Tecnicos.models import Tecnico
from apps.Tecnicos.forms import TecnicoForm

class TecList(ListView):
	model = Tecnico
	template_name = 'Tecnico/index.html'

class TecCreate(CreateView): 
	model = Tecnico
	form_class = forms.TecnicoForm
	template_name = 'Tecnico/nuevo.html'
	def get_success_url(self):
		return reverse('tec.index')

class TecActualizar(UpdateView): 
	model = Tecnico
	form_class = forms.TecnicoForm
	template_name = 'Tecnico/nuevo.html'
	def get_success_url(self):
		return reverse('tec.index')

class TecEliminar(DeleteView):
	model = Tecnico
	template_name = 'Tecnico/eliminar.html'
	def get_success_url(self):
		return reverse('mtto.index')
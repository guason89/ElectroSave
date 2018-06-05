from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.TipoEquipo import forms

from apps.TipoEquipo.models import TipoEquipo

class TipoEquipoList (ListView):
	model = TipoEquipo
	template_name = 'TipoEquipo/index.html'

class TipoEquipoCreate(CreateView):
	model = TipoEquipo
	form_class = forms.TipoEquipoForm
	template_name = 'TipoEquipo/nuevo.html' 
	
	def get_success_url(self):
		return reverse('tipo_equipo.index')

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Modelos.models import Instalacion

# Create your views here.
class InstalacionesList (ListView):
	model = Instalacion
	template_name = 'instalaciones/index.html'

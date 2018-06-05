from django.shortcuts import render
from apps.Equipos.models import Equipo

class EquipoList (ListView):
	model = Equipo
	template_name = 'Equipos/index.html'
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Modelos.models import Instalacion
from apps.Modelos.models import Equipos

from apps.Instalaciones.forms import InstalacionForm
from django.urls import reverse, reverse_lazy

# Create your views here.
class InstalacionesList (ListView):
	model = Instalacion
	template_name = 'instalaciones/index.html'

class InstalacionesActualizar(UpdateView):
	model = Instalacion
	form_class = InstalacionForm
	template_name = 'instalaciones/editar.html' 
	success_url = reverse_lazy('instalaciones.index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_instalacion = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_instalacion = identificador)
		form = self.form_class(request.POST, instance = modelo)
		if form.is_valid():		
			#se recupera el numero de serie
			num_serie = request.POST['num_serie']
			if len(num_serie) > 0:
				modelo.estatus_inst = 'REALIZADA'
				equipo = Equipos.objects.get(id_equipo = modelo.id_equipo)
				equipo.estado_e = 'INSTALADO'
				equipo.num_serie_e = num_serie
				equipo.save()
			modelo.save()
			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))
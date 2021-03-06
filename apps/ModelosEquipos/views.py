from django.shortcuts import render , redirect
#from django.http import HttpResponseRedirect

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from apps.ModelosEquipos.forms import EquipoForm
from apps.ModelosEquipos.models import ModeloEquipo
from apps.ModelosEquipos.models import TipoEquipo
from apps.Modelos.models import ProveedorModelos

class ModeloList (ListView):
	model = ModeloEquipo
	template_name = 'Modelos/index.html'


class ModeloCreate(CreateView):
	model = ModeloEquipo
	form_class = EquipoForm
	template_name = 'Modelos/nuevo.html' 
	success_url = reverse_lazy('modelos.index')
	#def get_success_url(self):
		#return reverse('modelos.index')

	def get_context_data(self, **kwargs):
		context = super(ModeloCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():			 
			id_tipo = request.POST['selecttipo']		
			modelo = form.save(commit=False)
			modelo.tipo = TipoEquipo.objects.get(id_tipo_equipo=id_tipo)
			modelo.save()
			#asignacion de proveedores de este modelo
			id_proveedores = request.POST.getlist('id_proveedores')
			for pr in id_proveedores:
				pm = ProveedorModelos(id_proveedor = pr, id_modelo = modelo.id_modelo)
				pm.save()
			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class ModeloUpdate(UpdateView):
	model = ModeloEquipo
	form_class = EquipoForm
	template_name = 'Modelos/nuevo.html'
	success_url = reverse_lazy('modelos.index')

	def get_context_data(self, **kwargs):
		context = super(ModeloUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_modelo = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_modelo = identificador)
		form = self.form_class(request.POST, instance = modelo)
		if form.is_valid():			 
			id_tipo = request.POST['selecttipo']			
			modelo.tipo = TipoEquipo.objects.get(id_tipo_equipo=id_tipo)
			modelo.save()
			#eliminacion de los objetos relacionados 
			proveedor_modelo = ProveedorModelos.objects.filter(id_modelo = modelo.id_modelo)
			for provmod in proveedor_modelo:
				provmod.delete()
			#asignacion de proveedores de este modelo
			id_proveedores = request.POST.getlist('id_proveedores')
			for pr in id_proveedores:
				pm = ProveedorModelos(id_proveedor = pr, id_modelo = modelo.id_modelo)
				pm.save()

			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class ModeloEquipoEliminar(DeleteView):
	model = ModeloEquipo
	template_name = 'Modelos/eliminar.html'
	success_url = reverse_lazy('modelos.index')

	def get_contexto_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_modelo = pk) #he dejado modelo como nombre genérico para Modelo
		if object not in context:				
			context['object'] = self.object			
			context['id'] = pk
			#print(kwargs)
			msj = kwargs.get('msj')			
			context['msj'] = msj
			
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_modelo = identificador)
		prov_asociados = ProveedorModelos.objects.filter(id_modelo = modelo.id_modelo)
		if len(prov_asociados) > 0:					
			kwargs['msj'] = 'No es posible eliminar el MODELO, desasocie los proveedores primero!'
			return self.render_to_response(self.get_contexto_data(**kwargs))
		else:
			modelo.delete()
			return redirect(self.get_success_url())
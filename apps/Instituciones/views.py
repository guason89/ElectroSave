from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Instituciones.forms import InstitucionForm
from django.urls import reverse, reverse_lazy

from apps.Modelos.models import Instituciones
from apps.Modelos.models import Compras
from apps.Modelos.models import Instalacion
from apps.Modelos.models import InstitucionProveedores
from apps.Modelos.models import Equipos

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
	template_name = 'Instituciones/editar.html' 
	success_url = reverse_lazy('instituciones.index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_institucion = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_institucion = identificador)
		form = self.form_class(request.POST, instance = modelo)
		if form.is_valid():			
			modelo.save()
			#eliminacion de los objetos relacionados 
			proveedores_asoc = InstitucionProveedores.objects.filter(id_institucion = modelo.id_institucion)
			for provmod in proveedores_asoc:
				provmod.delete()
			#asignacion de proveedores de este modelo
			id_proveedores = request.POST.getlist('id_proveedores')
			for pr in id_proveedores:
				pm = InstitucionProveedores(id_institucion = modelo.id_institucion, id_proveedor = pr)
				pm.save()

			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class InstitucionesEliminar(DeleteView):
	model = Instituciones
	template_name = 'Instituciones/eliminar.html'
	success_url=reverse_lazy('instituciones.index')

	def get_contexto_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_institucion = pk) #he dejado modelo como nombre genérico para Modelo
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
		modelo = self.model.objects.get(id_institucion = identificador)
		cp_asociados = Compras.objects.filter(id_institucion = modelo.id_institucion)
		if len(cp_asociados) > 0:					
			kwargs['msj'] = 'No es posible eliminar porque hay compras asociadas!'
			return self.render_to_response(self.get_contexto_data(**kwargs))
		else:
			modelo.delete()
			return redirect(self.get_success_url())

class InstitucionInstalacion(UpdateView):
	model = Instituciones
	form_class = InstitucionForm
	template_name = 'Instituciones/instalaciones.html' 
	success_url = reverse_lazy('instituciones.index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_institucion = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk
			context['msj'] = 'Ocurrió un error!'			
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_institucion = identificador)
		form = self.form_class(request.POST, instance = modelo)
		try:		
			#insert de detalle compra
			id_equipos = request.POST.getlist('id_equipos')
			id_proveedor = request.POST['proveedor']
			fecha = request.POST['fecha']
			for item in id_equipos:	
				eq = Equipos.objects.get(id_equipo = item)
				eq.estado_e = 'PROGRAMADO'
				eq.save()			
				pins = Instalacion(id_proveedor = id_proveedor, fecha_inst = fecha, estatus_inst = 'PROGRAMADO', id_equipo = item)
				pins.save()

			return redirect(self.get_success_url())
		except Exception as e:
			print(e)			
			return self.render_to_response(self.get_context_data(form=form))
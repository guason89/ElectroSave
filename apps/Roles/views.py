from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from django.urls import reverse, reverse_lazy

from apps.Modelos.models import AuthGroup, AuthGroupPermissions, AuthUserGroups
from apps.Roles.forms import RolesForm, RolesFormCreate

from django.db import connection

class RolesList (ListView):
	model = AuthGroup
	template_name = 'Roles/index.html'

class RolesCreate(CreateView):
	model = AuthGroup
	form_class = RolesFormCreate
	template_name = 'Roles/nuevo.html'	
	success_url = reverse_lazy('roles.index')

	def get_context_data(self, **kwargs):
		context = super(RolesCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():				
			modelo = form.save()
			id_permisos = request.POST.getlist('permisos')
			with connection.cursor() as cursor:				
				for per in id_permisos:
					cursor.execute("INSERT INTO auth_group_permissions(group_id,permission_id)values(%s,%s)", [modelo.id,per])

			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class RolesUpdate(UpdateView):
	model = AuthGroup
	form_class = RolesForm
	template_name = 'Roles/editar.html'	
	success_url= reverse_lazy('roles.index')

	def get_context_data(self, **kwargs):
		context = super(RolesUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			contex['id'] = pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id = identificador)
		form = self.form_class(request.POST, instance = modelo)
		if form.is_valid():			 
			id_permisos = request.POST.getlist('permisos')
			with connection.cursor() as cursor:
				cursor.execute("DELETE FROM auth_group_permissions WHERE group_id = %s", [identificador])
				for per in id_permisos:
					cursor.execute("INSERT INTO auth_group_permissions(group_id,permission_id)values(%s,%s)", [identificador,per])

			modelo.save() #se guarda la instancia del modelo
			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

'''class TipoEquipoDetalles(DetailView):
	model = TipoEquipo
	template_name = 'TipoEquipo/detalle.html'''

class RolesDelete(DeleteView):
	model = AuthGroup
	template_name = 'Roles/eliminar.html'
	success_url = reverse_lazy('roles.index')

	def get_contexto_data(self, **kwargs):		
		context = super(RolesDelete, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id = pk) #he dejado modelo como nombre genérico para Modelo
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
		modelo = self.model.objects.get(id = identificador)
		us_asociados = AuthUserGroups.objects.filter(group_id = modelo.id)
		if len(us_asociados) > 0:					
			kwargs['msj'] = 'No es posible eliminar el ROL porque tiene usuarios asociados!'
			return self.render_to_response(self.get_contexto_data(**kwargs))
		else:
			modelo.delete()
			return redirect(self.get_success_url())
	
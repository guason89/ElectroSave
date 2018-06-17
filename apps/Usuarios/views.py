from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from apps.Modelos.models import  AuthUser

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
from apps.Usuarios.forms import UsuarioForm, UsuarioFormUpdate, EmailForm
from django.urls import reverse, reverse_lazy

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.db import connection

def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class UsuarioList (ListView):
	model = AuthUser
	template_name = 'usuarios/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		with connection.cursor() as cursor:
			cursor.execute("SELECT au.id, au.username, au.first_name||' '||au.last_name nombre, au.email, is_active, ag.id rol_id, ag.name rol_name from auth_user au inner join auth_user_groups aug on au.id = aug.user_id inner join auth_group ag on aug.group_id = ag.id", [])
			results = dictfetchall(cursor) 
			context['object_list'] = results
		return context
class UsuarioCreate(CreateView):
	model = AuthUser
	form_class = UsuarioForm
	template_name = 'usuarios/nuevo.html' 
	success_url = reverse_lazy('usuarios.index')

	def get_context_data(self, **kwargs):
		context = super(UsuarioCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():			
			rol = request.POST['rol']		
			modelo = form.save(commit=False) #modelo es un objeto de usuario			
			modelo.set_password(modelo.password)
			modelo.save()
			
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO auth_user_groups(user_id,group_id)values(%s,%s)", [modelo.id,rol])

			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))


class UsuarioUpdate(UpdateView):
	model = AuthUser
	form_class = UsuarioFormUpdate
	template_name = 'usuarios/nuevo.html' 
	success_url = reverse_lazy('usuarios.index')

	def get_context_data(self, **kwargs):
		context = super(UsuarioUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id = pk)
		if 'authuser' not in context:
			context['authuser']	= modelo	
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk
				
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = User.objects.get(id = identificador)
		modelo_aux = self.model.objects.get(id = identificador)		
		form = self.form_class(request.POST, instance = modelo)	
		if form.is_valid():
			rol = request.POST['rol']	
			if len(request.POST['password']) > 0:
				modelo.set_password(request.POST['password'])
			else:
				modelo.password = modelo_aux.password
			modelo.save()
			
			'''with connection.cursor() as cursor:
				cursor.execute("DELETE FROM auth_user_groups WHERE user_id = %s", [identificador])
				cursor.execute("INSERT INTO auth_user_groups(user_id,group_id)values(%s,%s)", [modelo.id,rol])
			'''
			return redirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class UsuarioDetalles(DetailView):
	model = AuthUser
	template_name = 'usuarios/detalles.html'


#vista para enviar correo electronico
class SendEmail(TemplateView):	
	template_name = 'usuarios/email.html'
	#form_class = EmailForm

	def get_success_url():
		return reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		#context['form'] = self.form_class()
		msj = kwargs.get('msj')			
		context['msj'] = msj
		return context

	def post(self, request, *args, **kwargs):
		email = request.POST['email']
		usuario = AuthUser.objects.filter(email = email)	
		if len(usuario)>0:
			mensaje = request.POST['mensaje']
					
			body = render_to_string(
				'usuarios/email_content.html',
				{
				 'message':mensaje,
				 'email':email,
				},)

			email_message = EmailMessage(
				subject = 'ElectroSave solicitud de gestión de usuario',
				body = body,
				from_email = 'electrosave.gestion.usuario@gmail.com',
				to = ['mtbguason@hotmail.com'],
				)
			email_message.content_subtype = 'html'
			email_message.send()
			return redirect(SendEmail.get_success_url())
		else:
			kwargs['msj'] = 'No se encontró ningun usuario con el email proporcionado!'
			return self.render_to_response(self.get_context_data(**kwargs))

class SendEmailInterno(TemplateView):	
	template_name = 'usuarios/email2.html'

	def get_success_url():
		return reverse_lazy('home')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		return context

	def post(self, request, *args, **kwargs):
		email = request.POST['email']
		mensaje = request.POST['mensaje']
		nombres = request.POST['nombres']
		apellidos = request.POST['apellidos']			
					
		body = render_to_string(
			'usuarios/email_content2.html',
			{
			 'message':mensaje,
			 'email':email,
			 'nombres':nombres,
			 'apellidos':apellidos
			})

		email_message = EmailMessage(
			subject = 'ElectroSave solicitud de nuevo usuario',
			body = body,
			from_email = 'electrosave.gestion.usuario@gmail.com',
			to = ['4dministrador.3l3ctros4v3@gmail.com'],
			)
		email_message.content_subtype = 'html'
		email_message.send()
		return redirect(SendEmailInterno.get_success_url())
		
		




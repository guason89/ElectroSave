from django.shortcuts import render

from apps.Modelos.models import  AuthUser

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Usuarios.forms import UsuarioForm
from django.urls import reverse, reverse_lazy

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
'''class UsuarioCreate(CreateView):
	model = AuthUser
	form_class = UsuarioForm
	template_name = 'Usuarios/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('usuarios.index')'''

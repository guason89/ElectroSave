from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from apps.Proveedores import models
from apps.Proveedores import forms
from django.urls import reverse



class ProveedorList (ListView):
	model = models.Proveedor
	template_name = 'proveedores/index.html'

class ProveedorCreate (CreateView):
	model = models.Proveedor
	form_class = forms.ProveedorForm
	template_name = 'proveedores/nuevo.html' 
	
	def get_success_url(self):
		return reverse('proveedores.index')



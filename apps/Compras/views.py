from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.Compras.forms import ComprasForm
from django.urls import reverse, reverse_lazy

from apps.Modelos.models import Compras, DetCompras

class comprasList(ListView):
	model = Compras
	template_name = 'compras/index.html'

class comprasCreate(CreateView):
	model = Compras
	form_class = ComprasForm
	template_name = 'compras/nuevo.html' 
	
	def get_success_url(self):
		return reverse_lazy('compras.index')

class comprasActualizar(UpdateView):
	model = Compras
	form_class = ComprasForm
	template_name = 'compras/editar.html' 
	success_url = reverse_lazy('compras.index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		modelo = self.model.objects.get(id_compra = pk)
		if 'form' not in context:
			context['form'] = self.form_class()
			context['id'] = pk			
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		identificador = kwargs['pk']
		modelo = self.model.objects.get(id_compra = identificador)
		form = self.form_class(request.POST, instance = modelo)
		try:		
			#elimnar los detalles que tenia
			detalles = DetCompras.objects.filter(id_compra = modelo.id_compra)
			for det in detalles:
				det.delete()
			#insert de detalle compra
			id_detalles = request.POST.getlist('valor_item')
			for item in id_detalles:
				lista = item.split('||')
				valor = lista.pop()
				cantidad = lista.pop()
				id_mod = lista.pop()
				calculado = int(cantidad) * float(valor)
				dc = DetCompras(id_compra = modelo.id_compra, id_modelo = id_mod, cantidad = cantidad, valor_unidad = valor, total_item = calculado)
				dc.save()

			return redirect(self.get_success_url())
		except Exception as e:
			print(e)			
			return self.render_to_response(self.get_context_data(form=form))

class ComprasDetalles(DetailView):
	model = Compras
	template_name = 'compras/detalle.html' 

'''class comprasEliminar(DeleteView):
	model = compras
	template_name = 'compras/eliminar.html'
	def get_success_url(self):
		return reverse_lazy('instituciones.index')'''
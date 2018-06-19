from django import forms

from apps.Mantenimientos.models import Mantenimiento
from apps.Tecnicos.models import Tecnico

class MantenimientoForm(forms.ModelForm):
	list_tecnicos = Tecnico.objects.all()
	#llenamos el selecto
	opciones = [(tp.tecnico_id,tp.tecnico_nombre) for tp in list_tecnicos]
	mtto_fecha = forms.DateField(label='Fecha de Mtto', widget=forms.TextInput(attrs={'class':'form-control'}))
	mtto_fecha_prox = forms.DateField(label='Proximo Mtto', widget=forms.TextInput(attrs={'class':'form-control'}))
	mtto_estado_i = forms.CharField(label='Estado Inicial', widget=forms.TextInput(attrs={'class':'form-control'})) 
	mtto_estado_f = forms.CharField(label='Estado Final', widget=forms.TextInput(attrs={'class':'form-control'}))
	mtto_comentario = forms.CharField(label='Comentarios', widget=forms.Textarea(attrs={'class':'form-control'}))
	mtto_costo = forms.FloatField(label='Costo ($)', widget =forms.TextInput(attrs={'class':'form-control'}))
	tecnico_id = forms.ChoiceField(choices=opciones, widget=forms.Select(attrs={'class':'form-control'}))
	equipo_id = forms.CharField(label='Equipo ID', widget =forms.TextInput(attrs={'class':'form-control'}))
	
	class Meta:
		model = Mantenimiento
		fields = [
			'mtto_fecha',
			'mtto_fecha_prox',
			'mtto_estado_i',
			'mtto_estado_f',
			'mtto_comentario',
			'mtto_costo',
			'tecnico_id',
			'equipo_id',
		]
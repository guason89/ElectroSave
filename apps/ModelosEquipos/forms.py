from django import forms

from apps.ModelosEquipos.models import ModeloEquipo 
from apps.ModelosEquipos.models import TipoEquipo

class EquipoForm(forms.ModelForm):
	marca = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombre_modelo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	año_fabricacion = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class': 'form-control'}))	
	#capacidad_btu = forms.CharField(required = False, label='Capacidad BTU (Para aires acondicionados)',widget=forms.TextInput(attrs={'class': 'form-control'}))

	tipos = TipoEquipo.objects.all()
	#tipos = [('','-----')]
	#tipos += [(te.id_tipo_equipo,te.tipo_equipo) for te in TipoEquipo.objects.all()]
	#selecttipo= forms.ChoiceField(choices = tipos, widget=forms.Select(attrs={'class': 'form-control','required':'true'}))
	
	class Meta:
		model = ModeloEquipo			

		fields = [
		'marca',
		'nombre_modelo',
		'año_fabricacion',				
		'capacidad_btu'			
		]


	
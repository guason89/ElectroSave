from django import forms

from apps.Instituciones.models import Instituciones

class InstitucionForm(forms.ModelForm):
	#tipo_equipo = forms.CharField(max_length=250, label='NOMBRE TIPO DE EQUIPO',widget=forms.TextInput(attrs={'class': 'form-control','id':'tipo_equipo'}))
	nombre_inst = forms.CharField(max_length=250, label='NOMBRE INSTITUCION',widget=forms.TextInput(attrs={'class':'form-control'}))
	nit_inst = forms.CharField(max_length=15, label='NIT',widget=forms.TextInput(attrs={'class': 'form-control'}))
	telefono_1_inst = forms.CharField(max_length=12, label='TELEFONO 1', widget=forms.TextInput(attrs={'class':'form-control'}))
	telefono_2_inst = forms.CharField(max_length=12, label='TELEFONO 2',widget=forms.TextInput(attrs={'class':'form-control'}))
	complemento_dir = forms.CharField(max_length=250, label='DIRECCION',widget=forms.TextInput(attrs={'class': 'form-control'}))
	presupuesto = forms.CharField(max_length=15, label='PRESUPUESTO',widget=forms.TextInput(attrs={'class':'form-control'}))
		
	class Meta:
		model = Instituciones			

		fields = [
		'nombre_inst',
		'nit_inst',
		'telefono_1_inst',
		'telefono_2_inst',
		#'departamento_inst',
		#'municipio_inst',
		'complemento_dir',
		'presupuesto'
		]
from django import forms

from apps.Compras.models import Compras
from apps.Proveedores.models import Proveedor

class ComprasForm(forms.ModelForm):
	list_proveedores = Proveedor.objects.all()
	#tipo_equipo = forms.CharField(max_length=250, label='NOMBRE TIPO DE EQUIPO',widget=forms.TextInput(attrs={'class': 'form-control','id':'tipo_equipo'}))
	
	opciones = [(tp.id_proveedor,tp.nombre) for tp in list_proveedores]
	id_proveedor= forms.ChoiceField(choices = opciones, widget=forms.Select(attrs={'class': 'form-control','required':'true'}))
	fecha_compra = forms.CharField(max_length=15, label='FECHA COMPRA',widget=forms.TextInput(attrs={'class': 'form-control'}))
	tipo_contratacion = forms.CharField(max_length=12, label='TIPO DE CONTRATACION', widget=forms.TextInput(attrs={'class':'form-control'}))
	total_compra = forms.CharField(max_length=12, label='TOTAL COMPRA',widget=forms.TextInput(attrs={'class':'form-control'}))
	#total_bruto = forms.CharField(max_length=250, label='TOTAL BRUTO',widget=forms.TextInput(attrs={'class': 'form-control'}))
	#total_impuesto_1 = forms.CharField(max_length=15, label='IMPUESTO 1',widget=forms.TextInput(attrs={'class':'form-control'}))
	#total_impuesto_2 = forms.CharField(max_length=15, label='IMPUESTO 2',widget=forms.TextInput(attrs={'class':'form-control'}))		
	class Meta:
		model = Compras			
		fields = [
		'id_proveedor',
		'fecha_compra',
		'tipo_contratacion',
		'total_compra',
		#'total_bruto',
		#'total_impuesto_1',
		#'total_impuesto_2',
		]
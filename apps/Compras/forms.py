from django import forms

from apps.Modelos.models import Compras
from apps.Proveedores.models import Proveedor
from apps.Modelos.models import Instituciones, FormaContratacion

class ComprasForm(forms.ModelForm):
	list_proveedores = Proveedor.objects.all()
	list_instituciones = Instituciones.objects.all()
	list_forma_contratacion = FormaContratacion.objects.all()

	opciones_proveedores = [(tp.id_proveedor,tp.nombre) for tp in list_proveedores]
	opciones_instituciones = [(ins.id_institucion,ins.nombre_inst) for ins in list_instituciones]
	opciones_forma = [(forma.id_forma_cont,forma.descripcion_tc) for forma in list_forma_contratacion]

	id_proveedor= forms.ChoiceField(label='Proveedor', required = True, choices = opciones_proveedores, widget=forms.Select(attrs={'class': 'form-control'}))
	id_institucion = forms.ChoiceField(label='Institucion',required = True, choices = opciones_instituciones, widget=forms.Select(attrs={'class': 'form-control'}))
	id_tipo_cont = forms.ChoiceField(label='Forma Contratación',required = True, choices = opciones_forma, widget=forms.Select(attrs={'class': 'form-control'}))
	fecha_compra = forms.CharField(max_length=15, label='FECHA COMPRA',widget=forms.TextInput(attrs={'class': 'form-control datepicker2','data-date-format':"yyyy-mm-dd"}))	
	total_compra = forms.CharField(max_length=12, label='TOTAL COMPRA',widget=forms.TextInput(attrs={'class':'form-control'}))
	descripcion_compra = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))

	class Meta:
		model = Compras			
		fields = [
		'id_institucion',
		'id_proveedor',
		'fecha_compra',
		'id_tipo_cont',
		'total_compra',
		'descripcion_compra'
		]
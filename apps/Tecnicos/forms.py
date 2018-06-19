from django import forms

from apps.Tecnicos.models import Tecnico
from apps.Proveedores.models import Proveedor

class TecnicoForm(forms.ModelForm):
	list_proveedores = Proveedor.objects.all()
	opcionesTec = [(tp.id_proveedor, tp.nombre) for tp in list_proveedores]
	tecnico_nombre = forms.CharField(label='Nombre del Tecnico', widget=forms.TextInput(attrs={'class':'form-control'}))
	id_proveedor = forms.ChoiceField(choices=opcionesTec, widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Tecnico
		fields = [
			'tecnico_nombre',
			'id_proveedor',
		]
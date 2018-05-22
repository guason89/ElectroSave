from django import forms
from apps.Proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
		'nombre',
		'direccion',
		'numero_de_contacto',
		'email',
		'nit',
		]

		labels = {
			'nombre' : 'NOMRE',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'nombre'}),
			'direccion': forms.TextInput(attrs={'class':'form-control', 'id':'direccion'}),
			'numero_de_contacto': forms.TextInput(attrs={'class':'form-control', 'id':'numero_de_contacto'}),
			'email': forms.TextInput(attrs={'class':'form-control', 'id':'email'}),
			'nit': forms.TextInput(attrs={'class':'form-control', 'id':'nit'}),
		}


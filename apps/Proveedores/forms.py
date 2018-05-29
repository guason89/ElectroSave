from django import forms
from apps.Proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
	
	class Meta:
		model = Proveedor

		def clean_nombreProveedor(self):
			nombreProveedor = self.cleaned_data.get('nombre_proveedor')
			if (nombreProveedor != "nola"):
				raise forms.ValidationError("Deben de ser caractersalfanumerico")
			return nombre_proveedor	

		fields = [
		'nombre_proveedor',
		'direccion_proveedor',
		'nit_proveedor',
		'fecha_alta_proveedor',
		'telefono_proveedor'
		]


		labels = {
		'nombre_proveedor':'NOMBRE DEL PROVEEDOR',
		'direccion_proveedor': 'DIRECCIÓN DEL PROVEEDOR',
		'nit_proveedor':'NIT DEL PROVEEDOR',
		'fecha_alta_proveedor':'FECHA ALTA DEL PROVEEDOR',
		'telefono_proveedor':'TELEFONO DEL PROVEEDOR'
		}


		widgets = {
			'nombre_proveedor': forms.TextInput(attrs={'class':'form-control', 'id':'nombre_proveedor'}),
			'direccion_proveedor': forms.TextInput(attrs={'class':'form-control', 'id':'direccion_proveedor'}),
			'nit_proveedor': forms.TextInput(attrs={'class':'form-control', 'id':'nit_proveedor'}),
			'fecha_alta_proveedor': forms.TextInput(attrs={'class':'form-control', 'id':'fecha_alta_proveedor'}),
			'telefono_proveedor': forms.TextInput(attrs={'class':'form-control', 'id':'telefono_proveedor'}),
		}

		

	
	
  
from django import forms
from apps.Proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):

	Opciones = (
    ('S', ("SI")),
    ('N', ("NO"))
	)

	permiso_instalacion = forms.ChoiceField(choices = Opciones, label="", initial='', 
		widget=forms.Select(attrs={'class':'form-control', 'id':'permiso_instalacion'}), required=True)
	
	email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Proveedor

		def clean_nombreProveedor(self):
			nombreProveedor = self.cleaned_data.get('nombre')
			if (nombreProveedor != "nola"):
				raise forms.ValidationError("Deben de ser caractersalfanumerico")
			return nombre	

		fields = [
		'nombre',
	    'direccion',
	    'nit',
	    'fecha_alta_proveedor',
	    'telefono_1',
	    'telefono_2',
	    'permiso_instalacion',
	    'email',
	    'responsable'	
		]


		labels = {
		'nombre':'NOMBRE',
	    'direccion':'DIRECCIÓN',
	    'nit':'NIT',
	    'fecha_alta_proveedor':'FECHA ALTA',
	    'telefono_1':'TELEFONO 1',
	    'telefono_2':'TELEFONO 2',
	    'permiso_instalacion':'PERMISO DE INSTALCIÓN',
	    'email':'CORREO',
	    'responsable':'RESPONSABLE'	
		}

		widgets = {
		'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre'}),
	    'direccion':forms.TextInput(attrs={'class':'form-control', 'id':'direccion'}),
	    'nit':forms.TextInput(attrs={'class':'form-control', 'id':'nit'}),
	    'fecha_alta_proveedor':forms.TextInput(attrs={'class':'form-control datepicker2', 'data-date-format':'yyyy-mm-dd', 'id':'fecha_alta_proveedor'}),
	    'telefono_1':forms.TextInput(attrs={'class':'form-control', 'id':'telefono_1'}),
	    'telefono_2':forms.TextInput(attrs={'class':'form-control', 'id':'telefono_2'}),
	    #'permiso_instalacion':forms.ChoiceField(choices = Opciones,attrs={'class':'form-control', 'id':'permiso_instalacion'}),
	    #'email':forms.TextInput(attrs={'class':'form-control', 'id':'email'}),
	    'responsable':forms.TextInput(attrs={'class':'form-control', 'id':'responsable'})			
		}

		

	
	
  
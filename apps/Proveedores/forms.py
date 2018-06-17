from django import forms
from apps.Proveedores.models import Proveedor
from apps.ModelosEquipos.models import ModeloEquipo


class ProveedorForm(forms.ModelForm):
	
	email = forms.EmailField(label='CORREO ELECTRÓNICO', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	
	modelos = ModeloEquipo.objects.all()
	class Meta:
		model = Proveedor			

		fields = [
		'nombre',
	    'direccion',
	    'nit',	    
	    'telefono_1',
	    'telefono_2',
	    'email',
	    'responsable'	
		]


		labels = {
		'nombre':'NOMBRE',
	    'direccion':'DIRECCIÓN',
	    'nit':'NIT',
	    'telefono_1':'TELEFONO 1',
	    'telefono_2':'TELEFONO 2',	    
	    'responsable':'RESPONSABLE'	
		}

		widgets = {
		'nombre':forms.TextInput(attrs={'class':'form-control', 'id':'nombre'}),
	    'direccion':forms.TextInput(attrs={'class':'form-control', 'id':'direccion'}),
	    'nit':forms.TextInput(attrs={'class':'form-control', 'id':'nit'}),
	    'telefono_1':forms.TextInput(attrs={'class':'form-control', 'id':'telefono_1'}),
	    'telefono_2':forms.TextInput(attrs={'class':'form-control', 'id':'telefono_2'}),    
	    'responsable':forms.TextInput(attrs={'class':'form-control', 'id':'responsable'})			
		}

		

	
	
  
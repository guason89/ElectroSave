from django import forms

from apps.TipoEquipo.models import TipoEquipo

class TipoEquipoForm(forms.ModelForm):
	
	tipo_equipo = forms.CharField(max_length=250, label='NOMBRE TIPO DE EQUIPO',widget=forms.TextInput(attrs={'class': 'form-control','id':'tipo_equipo'}))
		
	class Meta:
		model = TipoEquipo			

		fields = [
		'tipo_equipo'	  	
		]

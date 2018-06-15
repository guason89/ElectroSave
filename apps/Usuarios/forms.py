from django import forms

from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
	
	username = forms.CharField(max_length=250, label='NOMBRE TIPO DE EQUIPO',widget=forms.TextInput(attrs={'class': 'form-control','id':'tipo_equipo'}))
		
	class Meta:
		model = User			

		fields = [
		'username'	  	
		]
from django import forms

from apps.Modelos.models import AuthGroup
from apps.Modelos.models import AuthPermission

class RolesForm(forms.ModelForm):
	
	name = forms.CharField(max_length=80, label='NOMBRE DE ROL',widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	permisos = AuthPermission.objects.all()

	class Meta:
		model = AuthGroup			

		fields = [
		'name'	  	
		]
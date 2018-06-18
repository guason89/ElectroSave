from django import forms

from apps.Modelos.models import AuthGroup
from apps.Modelos.models import AuthPermission


class RolesForm(forms.ModelForm):
	
	name = forms.CharField(max_length=80, label='NOMBRE DE ROL',widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	
	class Meta:
		model = AuthGroup			

		fields = [
		'name'	  	
		]

class RolesFormCreate(forms.ModelForm):
	
	name = forms.CharField(max_length=80, label='NOMBRE DE ROL',widget=forms.TextInput(attrs={'class': 'form-control'}))
	lista_exclude = [1,2,4,5,6]
	permisos = AuthPermission.objects.exclude(content_type_id__in=lista_exclude)
	
	class Meta:
		model = AuthGroup			

		fields = [
		'name'	  	
		]
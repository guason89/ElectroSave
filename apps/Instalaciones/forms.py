from django import forms

from apps.Modelos.models import Instalacion

class InstalacionForm(forms.ModelForm):
	
    
    fecha_inst = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control datepicker2','data-date-format':"yyyy-mm-dd"}))	  
    

    class Meta:
    	model = Instalacion

    	fields = [
		
		'fecha_inst',
		
		]


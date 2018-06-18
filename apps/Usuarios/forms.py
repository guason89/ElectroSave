from django import forms

from apps.Modelos.models import AuthGroup
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation 
import re
class UsuarioForm(forms.ModelForm):
	
	username = forms.CharField(max_length=150, label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(max_length=128, label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	confirm_password = forms.CharField(label = 'Confirme contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=30, label='Nombres',widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=150, label='Apellidos',widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))	

	roles = AuthGroup.objects.all()

	class Meta:
		model = User			

		fields = [
		'username',
		'password',		
		'first_name',
		'last_name',
		'email'
		]

	def clean_password(self):				
		password = self.cleaned_data.get("password")
		confirm_password = self.data['confirm_password'] #se obtiene de esta forma ya que no esta en los fields		
		if password != confirm_password:
			self.add_error('password', "La contraseña no coincide!")
		elif (re.match("^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$",password)) == None:
				self.add_error('password', "La contraseña Debe contener almenos 8 caracteres, llevar almenos una mayúscula, y un símbolo especial!")
		elif (re.match("[a-zA-Z]",password)) == None:
				self.add_error('password', "La contraseña debe iniciar con una letra!")
		return password

class UsuarioFormUpdate(forms.ModelForm):
	
	username = forms.CharField(max_length=150, label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(required = False,max_length=128, label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	confirm_password = forms.CharField(required = False,label = 'Confirme contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=30, label='Nombres',widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=150, label='Apellidos',widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))	

	roles = AuthGroup.objects.all()

	class Meta:
		model = User			

		fields = [
		'username',
		'password',		
		'first_name',
		'last_name',
		'email',
		'is_active'
		]

	def clean_password(self):		
		password = self.cleaned_data.get("password")
		confirm_password = self.data['confirm_password'] #se obtiene de esta forma ya que no esta en los fields
		if len(password) > 0 and len(confirm_password) > 0:
			if password != confirm_password:
				self.add_error('password', "La contraseña no coincide!")
			elif (re.match("^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$",password)) == None:
				self.add_error('password', "La contraseña Debe contener almenos 8 caracteres, llevar almenos una mayúscula, y un símbolo especial!")
			elif (re.match("[a-zA-z]",password)) == None:
				self.add_error('password', "La contraseña debe iniciar con una letra!")
		return password

#formulario para email
class EmailForm(forms.Form):	

	fields = [
		'email'		
	]

	def clean_email(self):
		email = self.data['email']
		
		usuario = User.objects.filter(email = email)

		if len(usuario) < 5: #no recupero usuario
			self.add_error('email', "No hay ningun usuario registrado con el email proporcionado!")
		return email



		
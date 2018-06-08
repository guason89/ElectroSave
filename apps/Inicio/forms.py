from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input100','placeholder':'Usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input100','placeholder':'Contraseña'}))
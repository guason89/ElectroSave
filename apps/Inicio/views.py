from django.template import RequestContext
from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy, reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

#para los procedimientos almacenados
from django.db import connection
from collections import namedtuple

from apps.Inicio.forms import LoginForm

#para devolver por nombre de columnas
def namedtuplefetchall(cursor):    
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def LogueoView(request):
	msj = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password) #tambien comprueba si está activo
			if user is not None: #si devuelve un usuario				
				login(request,user)					
				return redirect('home') #redirecciona a la pagina de inicio				
			else: #no retorna usuario, se llama el procedimientos logueo_function
				
				with connection.cursor() as cursor:
					cursor.callproc('logueo_function', [username])
					results = namedtuplefetchall(cursor)
					
				msj = results[0].logueo_function
	else:
		form = LoginForm()

	return render(request,'login.html',{'message':msj, 'form':form})

def LogoutView(request):
	logout(request)
	return redirect('login')

@login_required
def Home(request):
	return render(request,'home.html')




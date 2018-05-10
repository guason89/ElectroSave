from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(resquest):
	return render(resquest,'master.html')

def Loguear(resquest):
	return render(resquest,'login.html')
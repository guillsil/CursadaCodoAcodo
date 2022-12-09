from django.shortcuts import render,HttpResponse
from servicios.models import Servicio
from blog.models import Post

def home(request):
	return render(request,"home.html")

def servicios(request):
	servicios=Servicio.objects.all()
	return render(request,"servicios.html",{"servicios":servicios})

def blog(request):
	posts=Post.objects.all()
	return render(request,"blog.html",{"posts":posts})

def tienda(request):
	return render(request,"tienda.html")

def contacto(request):
    return render(request,"contacto.html")
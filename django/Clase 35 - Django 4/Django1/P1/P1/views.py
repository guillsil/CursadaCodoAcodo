from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.shortcuts import render
from django.template.loader import get_template

def saludo(request):
    nombre="Juan"
    return render(request,"Django\Templates\plantilla.html",{"nombre_persona":nombre})
    apellido= "Gonzalez"
    return render(request,"Django\Templates\plantilla.html",{"apellido_persona":apellido})
    fecha = datetime.datetime.now()
    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def saludo_html(request):
    arch=open("Django\P1\plantilla.html")
    plt=Template(arch.read())
    arch.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)
    
def despedida(request):
    return HttpResponse("Hasta luego!")
    


import datetime
def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,agno):
    periodo=agno-2020
    edad_futura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años"%(agno,edad_futura)
    return HttpResponse(documento)

def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"Django\Templates\curso.html",{"now":fecha})

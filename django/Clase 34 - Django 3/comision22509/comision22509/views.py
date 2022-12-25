from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader # Para cargar plantillas
from django.template.loader import get_template # Para cargar plantillas
from django.shortcuts import render # Para cargar plantillas    



def saludo(request):
    temas = ["Guillermo", "Silva", "Codo a Codo", "Python", "Django", "HTML"]
    fecha = datetime.datetime.now()
    return render(request, "plantilla.html", {"nombre": "Guillermo", "apellido": "Silva", "edad": 20, "now": fecha, "temas_curso": temas})


def saludohtml(request):
    documento = """<html><body><h1>Hola mundo </h1></body></html>"""
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Chaucito!")


def vista_nueva(request):
    return HttpResponse("Ultimo mensaje de prueba")


def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html><body><h1>Fecha actual: %s </h1></body></html>""" % fecha_actual
    return HttpResponse(documento)


def calcular_edad(request, edad, anio):
    periodo = anio - 2022
    nueva_edad = edad+periodo
    documento = """<html><body><h1>En el año %s vas a tener %s años. </h1></body></html>""" % (
        anio, nueva_edad)
    return HttpResponse(documento)

def curso(request):
    fecha = datetime.datetime.now()
    return render(request, "curso.html", {"now": fecha})  

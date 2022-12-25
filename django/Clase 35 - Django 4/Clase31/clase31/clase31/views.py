from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime


def saludo(request):
    nombre = "Pedro"
    apellido = "Gonzalez"
    fecha = datetime.datetime.now()
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas"]

    return render(request, "plantilla.html", {"nombre_persona": nombre,
                  "apellido_persona": apellido, "now": fecha,
                                              "temas_curso": temas})


def saludo_html(request):
    documento = """<html><body><h1>Hola mundo</h1></body></html>"""
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Adios mundo")


def getfecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html><body><h1>Fecha: %s</h1></body></html>""" % fecha_actual
    return HttpResponse(documento)


def calcular_edad(request, edad, agno):
    periodo = agno-2022
    edad_futura = edad+periodo
    documento = "<html><body><h2>En el año %s tendrás %s años" % (
        agno, edad_futura)
    return HttpResponse(documento)


def curso(request):
    fecha = datetime.datetime.now()
    return render(request, "curso.html", {"now": fecha})

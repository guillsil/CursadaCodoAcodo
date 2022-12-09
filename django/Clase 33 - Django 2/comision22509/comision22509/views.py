from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):

    fecha = datetime.datetime.now()
    archivo = open("C:/Users/Andres/OneDrive/Documentos/GitHub/CursadaCodoAcodo/django/Clase 33 - Django 2/comision22509/templates/plantilla.html")
    doc = Template(archivo.read())
    archivo.close()
    ctx = Context({"nombre": "Guillermo", "apellido": "Silva",
                  "edad": 20, "now": fecha})
    documento = doc.render(ctx)
    return HttpResponse(documento)


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

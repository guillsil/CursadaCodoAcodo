from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola mundo desde una view!")


def saludohtml(request):
    documento = """<html><body><h1>Hola Guillermo</h1></body></html>"""
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Chaucito!")

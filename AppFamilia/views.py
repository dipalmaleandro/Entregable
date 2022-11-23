from django.shortcuts import render
from .models import Integrantes
from django.http import HttpResponse
from django.template import Template,Context,loader

# Create your views here.
def integrantes(request):
    persona=Integrantes(nombre="Leandro ", apellido="DiPalma ", documento="28711888", ocupacion="Administrativo")
    persona.save()
    cadena_texto=persona
    return HttpResponse(cadena_texto)

def familiahtml (request):
    archivo=open("template1.html")
    template=Template(archivo.read())
    archivo.close
    contexto=Context(integrantes)
    documento=template.render(contexto)
    return HttpResponse(documento)

def familia1html (request):
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(integrantes)
    return HttpResponse(documento)


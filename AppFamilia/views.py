from django.shortcuts import render
from .models import Integrantes
from django.http import HttpResponse
from django.template import Template,Context,loader

# Create your views here.
def integrante1(request):
    persona1=Integrantes(nombre="Leandro ", apellido="DiPalma ", documento="28711888", ocupacion="Administrativo")
    persona1.save()
    cadena_texto=persona1
    return HttpResponse(cadena_texto)

def integrante2(request):
    persona2=Integrantes(nombre="Eliana ", apellido="Alarcon ", documento="30911908", ocupacion="Estilista")
    persona2.save()
    cadena_texto=persona2
    return HttpResponse(cadena_texto)

def integrante3(request):
    persona3=Integrantes(nombre="Santino ", apellido="DiPalma ", documento="40501888", ocupacion="Estudiante")
    persona3.save()
    cadena_texto=persona3
    return HttpResponse(cadena_texto)

def familiahtml (request):
    archivo=open("template1.html")
    template=Template(archivo.read())
    archivo.close
    contexto=Context(Integrantes)
    documento=template.render(contexto)
    return HttpResponse(documento)

def familia1html (request):
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(Integrantes)
    return HttpResponse(documento)


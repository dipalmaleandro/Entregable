from django.shortcuts import render
from .models import Integrantes1, Integrantes2, Integrantes3
from django.http import HttpResponse
from django.template import Template,Context,loader

# Create your views here.
def integrante1(request):
    persona1=Integrantes1(nombre="Leandro ", apellido="DiPalma ", documento="28711888", ocupacion="Administrativo")
    persona1.save()
    cadena_texto=persona1
    return HttpResponse(cadena_texto)

def integrante2(request):
    persona2=Integrantes2(nombre="Eliana ", apellido="Alarcon ", documento="30911908", ocupacion="Estilista")
    persona2.save()
    cadena_texto=persona2
    return HttpResponse(cadena_texto)

def integrante3(request):
    persona3=Integrantes3(nombre="Santino ", apellido="DiPalma ", documento="40501888", ocupacion="Estudiante")
    persona3.save()
    cadena_texto=persona3
    return HttpResponse(cadena_texto)

def familiahtml (request):
    archivo=open("template1.html")
    template=Template(archivo.read())
    archivo.close
    contexto=Context(Integrantes1)
    documento=template.render(contexto)
    return HttpResponse(documento)

def familia1html (request):
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(Integrantes1)
    return HttpResponse(documento)


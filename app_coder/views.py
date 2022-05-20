from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Curso
from django.template import loader

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    dicc = { "cursos" : cursos}
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso(request,nombre,camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    texto = f"Se guardo en la Base de Datos. Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

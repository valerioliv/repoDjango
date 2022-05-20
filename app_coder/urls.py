from django.urls import path
from . import views

urlpatterns = [
    path("cursos/", views.cursos),
    path("alta_curso/<nombre>/<camada>", views.alta_curso)
]
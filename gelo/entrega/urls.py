from django.urls import path
from .views import home,salvar, listaEntregas
urlpatterns = [
    path('',home),
    path('salvar',salvar, name='salvar'),
    path('encomendas',listaEntregas, name='listaEntregas'),
]
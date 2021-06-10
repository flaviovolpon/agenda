from django.shortcuts import render, redirect
from core.models import Evento
from core import models

# Create your views here.
# def index(request):
#     return redirect('/agenda')

def lista_eventos(request):
    # usuario = request.user
    # eventos = Evento.objects.filter(usuario=usuario)
    eventos = Evento.objects.all()
    dados = {'eventos':eventos}
    return render(request, 'agenda.html', dados)
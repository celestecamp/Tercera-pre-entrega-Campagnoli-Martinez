from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
#from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")


#__________________________________Jugadores
class jugadorList(ListView):
    model = Jugador

class jugadorCreate(CreateView):
    model = Jugador
    fields = ["nombre", "apellido", "posicion", "nacimiento", "altura", "pais"]
    success_url = reverse_lazy("jugadores")

class jugadorUpdate(UpdateView):
    model = Jugador
    fields = ["nombre", "apellido", "posicion", "nacimiento", "altura", "pais"]
    success_url = reverse_lazy("jugadores")

class jugadorDelete(DeleteView):
    model = Jugador
    success_url = reverse_lazy("jugadores")


#__________________________________Árbitros
class arbitroList(ListView):
    model = Arbitro

class arbitroCreate(CreateView):
    model = Arbitro
    fields = ["nombre", "apellido", "nacimiento", "pais"]
    success_url = reverse_lazy("arbitros")

class arbitroUpdate(UpdateView):
    model = Arbitro
    fields = ["nombre", "apellido", "nacimiento", "pais"]
    success_url = reverse_lazy("arbitros")

class arbitroDelete(DeleteView):
    model = Arbitro
    success_url = reverse_lazy("arbitros")


#__________________________________Jugadores
class equipoList(ListView):
    model = Equipo

class equipoCreate(CreateView):
    model = Equipo
    fields = ["nombre", "duenio", "fundacion", "titulos"]
    success_url = reverse_lazy("equipos")
       
class equipoUpdate(UpdateView):
    model = Equipo
    fields = ["nombre", "duenio", "fundacion", "titulos"]
    success_url = reverse_lazy("equipos")

class equipoDelete(DeleteView):
    model = Equipo
    success_url = reverse_lazy("equipos")

#__________________________________Buscar
def buscarJugadores(request):
    return render(request, "aplicacion/buscar.html")

def encontrar_jugadores(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        jugadores = Jugador.objects.filter(
            Q(nombre__icontains=patron.capitalize()) | 
            Q(apellido__icontains=patron.capitalize()) | 
            Q(posicion__icontains=patron.capitalize()) |
            Q(pais__icontains=patron.capitalize())
        )

        contexto = {"jugador_list": jugadores}
        return render(request, "aplicacion/jugador_list.html", contexto)
    
    else:
        contexto = {"jugador_list": Jugador.objects.all()}
        return render(request, "aplicacion/jugador_list.html", contexto)
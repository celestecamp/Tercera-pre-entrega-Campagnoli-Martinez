from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
#from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")


#__________________________________Jugadores
def jugadores(request):
    contexto = Jugador.objects.all()
    return render(request, "aplicacion/jugadores.html", {"jugadores": contexto})

def jugadoresForm(request):
    if request.method == "GET":
        miForm = JugadorForm()
        return render(request, "aplicacion/jugadorForm.html", {"form": miForm})
    else:
        miForm = JugadorForm(request.POST)
        if miForm.is_valid():
            juga_nombre = miForm.cleaned_data.get("nombre")
            juga_apellido = miForm.cleaned_data.get("apellido")
            juga_nac = miForm.cleaned_data.get("nacimiento")
            juga_pais = miForm.cleaned_data.get("pais")
            juga_pos = miForm.cleaned_data.get("posicion")
            juga_altura = miForm.cleaned_data.get("altura")

            juga = Jugador(nombre=juga_nombre.capitalize(),
                           apellido = juga_apellido.capitalize(),
                           nacimiento = juga_nac,
                           pais = juga_pais.capitalize(),
                           posicion = juga_pos.capitalize(),
                           altura = juga_altura)
            juga.save()

            contexto = Jugador.objects.all()
            return render(request, "aplicacion/jugadores.html", {"jugadores": contexto})


#__________________________________Árbitros
def arbitros(request):
    contexto = Arbitro.objects.all()
    return render(request, "aplicacion/arbitros.html", {"arbitros": contexto})

def arbitrosForm(request):
    if request.method == "GET":
        miForm = ArbitroForm()
        return render(request, "aplicacion/arbitroForm.html", {"form": miForm})
    else:
        miForm = ArbitroForm(request.POST)
        if miForm.is_valid():
            ar_nombre = miForm.cleaned_data.get("nombre")
            ar_apellido = miForm.cleaned_data.get("apellido")
            ar_nac = miForm.cleaned_data.get("nacimiento")
            ar_pais = miForm.cleaned_data.get("pais")

            arbi = Arbitro(nombre=ar_nombre.capitalize(),
                           apellido = ar_apellido.capitalize(),
                           nacimiento = ar_nac,
                           pais = ar_pais.capitalize())
            arbi.save()

            contexto = Arbitro.objects.all()
            return render(request, "aplicacion/arbitros.html", {"arbitros": contexto})


#__________________________________Jugadores
def equipos(request):
    contexto = Equipo.objects.all()
    return render(request, "aplicacion/equipos.html", {"equipos": contexto})

def equiposForm(request):
    if request.method == "GET":
        miForm = EquipoForm()
        return render(request, "aplicacion/equipoForm.html", {"form": miForm})
    else:
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            eq_nombre = miForm.cleaned_data.get("nombre")
            eq_duenio = miForm.cleaned_data.get("duenio")
            eq_fund = miForm.cleaned_data.get("fundacion")
            eq_titulos = miForm.cleaned_data.get("titulos")

            equi = Equipo(nombre=eq_nombre.capitalize(),
                           duenio = eq_duenio.capitalize(),
                           fundacion = eq_fund,
                           titulos = eq_titulos)
            equi.save()

            contexto = Equipo.objects.all()
            return render(request, "aplicacion/equipos.html", {"equipos": contexto})
        
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

        contexto = {"jugadores": jugadores}
        return render(request, "aplicacion/jugadores.html", contexto)
    
    else:
        contexto = {"jugadores": Jugador.objects.all()}
        return render(request, "aplicacion/jugadores.html", contexto)
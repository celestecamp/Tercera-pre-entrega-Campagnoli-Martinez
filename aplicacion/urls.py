from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #_____________________________Jugadores
    path('jugadores/', jugadores, name="jugadores"),
    path('agregar-jugador/', jugadoresForm, name="JugadorForm"),
    path('buscar-jugador/', buscarJugadores, name="buscar"),
    path('encontrar-jugador/', encontrar_jugadores, name="encontrar_jugadores"),

    #_____________________________Arbitros
    path('arbitros/', arbitros, name="arbitros"),
    path('agregar-arbitro/', arbitrosForm, name="ArbitroForm"),

    #_____________________________Equipos
    path('equipos/', equipos, name="equipos"),
    path('agregar-equipo/', equiposForm, name="EquipoForm"),
]

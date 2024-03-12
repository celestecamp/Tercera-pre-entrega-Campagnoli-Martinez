from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #_____________________________Jugadores
    path('jugadores/', jugadorList.as_view(), name="jugadores"),
    path('agregar-jugador/', jugadorCreate.as_view(), name="jugador_create"),
    path('editar-jugador/<int:pk>/', jugadorUpdate.as_view(), name="jugador_edit"),
    path('borrar-jugador/<int:pk>/', jugadorDelete.as_view(), name="jugador_delete"),
    path('buscar-jugador/', buscarJugadores, name="buscar"),
    path('encontrar-jugador/', encontrar_jugadores, name="encontrar_jugadores"),

    #_____________________________Arbitros
    path('arbitros/', arbitroList.as_view(), name="arbitros"),
    path('agregar-arbitro/', arbitroCreate.as_view(), name="arbitro_create"),
    path('editar-arbitro/<int:pk>/', arbitroUpdate.as_view(), name="arbitro_edit"),
    path('borrar-arbitro/<int:pk>/', arbitroDelete.as_view(), name="arbitro_delete"),

    #_____________________________Equipos
    path('equipos/', equipoList.as_view(), name="equipos"),
    path('agregar-equipo/', equipoCreate.as_view(), name="equipo_create"),
    path('editar-equipo/<int:pk>/', equipoUpdate.as_view(), name="equipo_edit"),
    path('borrar-equipo/<int:pk>/', equipoDelete.as_view(), name="equipo_delete"),
]

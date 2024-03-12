from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    pais = models.CharField(max_length = 30)
    posicion = models.CharField(max_length=30)
    altura = models.IntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

class Arbitro(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    pais = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    duenio = models.CharField(max_length=60)
    fundacion = models.IntegerField()
    titulos = models.IntegerField()

    def __str__(self):
        return self.nombre
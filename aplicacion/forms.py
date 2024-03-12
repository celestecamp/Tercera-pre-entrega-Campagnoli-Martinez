from django import forms 

class JugadorForm(forms.Form):
    #datos que pido en el form
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    nacimiento = forms.DateField(required=True)
    pais = forms.CharField(max_length = 30, required=True)
    posicion = forms.CharField(max_length=30, required=True)
    altura = forms.IntegerField(required=True)

class ArbitroForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    nacimiento = forms.DateField(required=True)
    pais = forms.CharField(max_length = 30, required=True)

class EquipoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    duenio = forms.CharField(max_length=60, required=True)
    fundacion = forms.IntegerField(required=True)
    titulos = forms.IntegerField(required=True)
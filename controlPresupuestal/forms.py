from django import forms
from .models import *

class MesCreateForm(forms.ModelForm):
	class Meta:
		model = Mes
		fields = ( 'mes','monto_autorizado',)

class MesEditForm(forms.ModelForm):
	class Meta:
		model = Mes
		fields = ( 'monto_ampliacion','monto_reduccion', 'monto_ejercido',)

class PartidaCreateForm(forms.ModelForm):
	class Meta:
		model = Partida
		fields = ( 'codigo','descripcion',)

class CapituloCreateForm(forms.ModelForm):
	class Meta:
		model = Capitulo
		fields = ( 'codigo',)
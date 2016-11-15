from django import forms
from .models import *

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ('codigo', 'capitulo', 'descripcion', 'monto_anual_autorizado', 
        	'monto_enero_autorizado', 'monto_febrero_autorizado', 'monto_marzo_autorizado', 
        	'monto_abril_autorizado', 'monto_mayo_autorizado', 'monto_junio_autorizado', 
        	'monto_julio_autorizado', 'monto_agosto_autorizado', 'monto_septiembre_autorizado', 
        	'monto_octubre_autorizado', 'monto_noviembre_autorizado', 'monto_diciembre_autorizado',)

class PartidaEditForm(forms.ModelForm):        
    class Meta:
        model = Partida
        fields = ('monto_enero_ampliacion', 'monto_enero_reduccion', 'monto_enero_ejercido', 
        	'monto_febrero_ampliacion', 'monto_febrero_reduccion', 'monto_febrero_ejercido',
        	'monto_marzo_ampliacion', 'monto_marzo_reduccion', 'monto_marzo_ejercido',
        	'monto_abril_ampliacion', 'monto_abril_reduccion', 'monto_abril_ejercido',
        	'monto_mayo_ampliacion', 'monto_mayo_reduccion', 'monto_mayo_ejercido',
        	'monto_junio_ampliacion', 'monto_junio_reduccion', 'monto_junio_ejercido',
        	'monto_julio_ampliacion', 'monto_julio_reduccion', 'monto_julio_ejercido',
        	'monto_agosto_ampliacion', 'monto_agosto_reduccion', 'monto_agosto_ejercido',
        	'monto_septiembre_ampliacion', 'monto_septiembre_reduccion', 'monto_septiembre_ejercido',
        	'monto_octubre_ampliacion', 'monto_octubre_reduccion', 'monto_octubre_ejercido',
        	'monto_noviembre_ampliacion', 'monto_noviembre_reduccion', 'monto_noviembre_ejercido',
        	'monto_diciembre_ampliacion', 'monto_diciembre_reduccion', 'monto_diciembre_ejercido',
        	)
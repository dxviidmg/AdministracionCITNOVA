from django import forms
from .models import *

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ('codigo', 'capitulo', 'descripcion', 'monto_anual_autorizado', 'monto_enero_autorizado', 'monto_febrero_autorizado', 'monto_marzo_autorizado', 'monto_abril_autorizado', 'monto_mayo_autorizado', 'monto_junio_autorizado', 'monto_julio_autorizado', 'monto_agosto_autorizado', 'monto_septiembre_autorizado', 'monto_octubre_autorizado', 'monto_noviembre_autorizado', 'monto_diciembre_autorizado',)
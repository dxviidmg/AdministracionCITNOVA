from django import forms
from .models import *
from accounts.models import *
#from . import views
from django.forms.widgets import Select
from django.contrib.auth.models import User
 
class SolicitudRecursoFinancieroPropioCreateForm(forms.ModelForm):
	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('concepto', 'importe_numero', 'importe_letra', 'metodo_pago')

class SolicitudRecursoFinancieroEmpleadoCreateForm(forms.ModelForm):

	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('a_nombre_de','concepto', 'importe_numero', 'importe_letra', 'metodo_pago')

	def __init__(self, departamento=None, **kwargs):
		super(SolicitudRecursoFinancieroEmpleadoCreateForm, self).__init__(**kwargs)
		if departamento:
			self.fields['a_nombre_de'].queryset=Perfil.objects.filter(departamento=departamento)
from django import forms
from .models import *
from accounts.models import *
#from . import views
from django.forms.widgets import Select
#from django.contrib.auth.models import User
 
class SolicitudRecursoFinancieroPropioCreateForm(forms.ModelForm):
	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('concepto', 'importe_numero', 'importe_letra', 'metodo_pago')

class SolicitudRecursoFinancieroEmpleadoCreateForm(forms.ModelForm):

	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('a_nombre_de','concepto', 'importe_numero', 'importe_letra', 'metodo_pago')
		#CHOICES = Perfil.objects.all(user=self.instance.user)
		Perfil_CHOICES = Perfil.objects.all()
		widgets = {
			'a_nombre_de': Select(choices=( (perfil.id, perfil.user) for perfil in Perfil_CHOICES)),
		}
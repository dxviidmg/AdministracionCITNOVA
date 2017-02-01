from django import forms
from django.contrib.auth.models import User
from .models import *

class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email',)

class PerfilEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('departamento', 'grado_profesional', 'puesto', 'telefono', 'banco', 'cta_bancaria')

#	def __init__(self, *args, **kwargs):
#		super(PerfilEmpleadoCreateForm, self).__init__(*args, **kwargs)
#		self.fields['grado_profesional'].choices = GE_CHOICES

class PerfilProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'telefono', 'banco', 'cta_bancaria')

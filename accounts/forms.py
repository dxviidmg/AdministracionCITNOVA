from django import forms
from django.contrib.auth.models import User
from .models import *

class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'departamento')

class PerfilEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'puesto', 'telefono', 'banco', 'cuenta_bancaria', 'CLABE')

#	def __init__(self, *args, **kwargs):
#		super(PerfilEmpleadoCreateForm, self).__init__(*args, **kwargs)
#		self.fields['grado_profesional'].choices = GE_CHOICES

class PerfilProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'telefono', 'banco', 'cuenta_bancaria', 'CLABE')

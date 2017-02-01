from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Departamento(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Banco(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Perfil(models.Model):

	GE_CHOICES = {
		("Tecnico", "Tecnico"),
		("T. S. U.", "T. S. U."),
		("Lic.", "Lic."),
		("Ing.", "Ing."),
		("Mtro(a).", "Mtro(a)."),
		("Dr.", "Dr."),
	}
	user = models.OneToOneField(User)
	grado_profesional = models.CharField(max_length=30, choices=GE_CHOICES, blank=True, null=True)
	puesto = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=10)
	banco = models.ForeignKey(Banco, blank=True, null=True)
	cta_bancaria = models.CharField(max_length=16, blank=True, null=True)
	departamento = models.ForeignKey(Departamento, blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)

	class Meta:
		ordering = ['user']
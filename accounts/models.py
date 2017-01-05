
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Area(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

class Perfil(models.Model):

	Tipo_CHOICES = {
		(1, "Interno"),
		(2, "Proveedor")
	}

	Banco_CHOICES = {
		("", "Ninguno"),
		("Banamex", "Banamex"),
		("BBVA Bancomer", "BBVA Bancomer"),
		("Santander", "Santander"),
		("HSBC", "HSBC"),
		("Inbursa", "Inbursa"),
		("ScotiaBank Inverlat", "ScotiaBank Inverlat"),
		("Banamex", "Banamex"),
		("American Express", "American Express"),
	}

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
	banco = models.CharField(max_length=30, choices=Banco_CHOICES)
	cta_bancaria = models.CharField(max_length=16, blank=True, null=True)
	tipo = models.IntegerField(choices=Tipo_CHOICES)
	area = models.ForeignKey(Area)

	def __str__(self):
		return '{}'.format(self.user)
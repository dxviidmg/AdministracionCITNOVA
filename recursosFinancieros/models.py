from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils import timezone

class SolicitudRecursoFinanciero(models.Model):
	MetodoPago_CHOICES = {
		("CHEQUE", "CHEQUE"),
		("TRANSFERENCIA ELECTRÓNICA", "TRANSFERENCIA ELECTRÓNICA")
	}
	folio = models.CharField(max_length=10, blank=True, null=True)
	#a_nombre_de = models.CharField(max_length=100, blank=True, null=True)
	a_nombre_de = models.ForeignKey(User, null=True, related_name="a_nombre_de")
	concepto = models.CharField(max_length=100, blank=True, null=True)
	importe_numero = models.DecimalField(max_digits=20,decimal_places=2)
	importe_letra = models.CharField(max_length=100)
	metodo_pago = models.CharField(max_length=30, choices= MetodoPago_CHOICES)
	clabe = models.CharField(max_length=100, blank=True, null=True)
	creacion = models.DateTimeField(default=timezone.now)
	solicitante = models.ForeignKey(User, null=True, related_name="solicitante")

	class Meta:
		ordering = ['folio']

	def __str__(self):
		return '{}'.format(self.folio)
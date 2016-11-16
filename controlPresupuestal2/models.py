from django.db import models
from decimal import Decimal
from django.utils import timezone

class Programa(models.Model):
	Fuente_CHOICES = (
		(1 , 'Federal'),
		(2 , 'Estatal'),
		(3 , 'Propios'),
	)
	nombre = models.CharField(max_length=150)
	objetivo = models.TextField()
	actividad = models.TextField()
	meta = models.IntegerField()
	unidad_de_medida = models.CharField(max_length=50)
	fuente_de_financiamiento = models.IntegerField(choices=Fuente_CHOICES)
	beneficiarios = models.TextField()
	oficio_de_autorizacion = models.CharField(max_length=20)
	año = models.IntegerField()
	fecha_creado = models.DateTimeField(default=timezone.now)
	monto = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	def __str__(self):
		return self.nombre

class Partida(models.Model):
	Capitulo_CHOICES = (
		(1000 , '1000 - Servicios personales'),
		(2000 , '2000 - Materiales y suministros'),
		(3000 , '3000 - Servicios generales'),
		(4000 , '4000 - Transferencias, asignaciones, subsidios y otras ayudas'),
	)
	programa = models.ForeignKey(Programa)
	capitulo = models.IntegerField(null=True, blank=True, choices=Capitulo_CHOICES)
	codigo = models.IntegerField()
	descripcion = models.TextField()	
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	def __str__(self):
		return '{} {}'.format(self.codigo, self.descripcion)

class Mes(models.Model):
	
	Mes_CHOICES = (
		(1 , 'Enero'),
		(2 , 'Febrero'),
		(3 , 'Marzo'),
		(4 , 'Abril'),
		(5 , 'Mayo'),
		(6 , 'Junio'),
		(7 , 'Julio'),
		(8 , 'Agosto'),
		(9 , 'Septiembre'),
		(10 , 'Octubre'),
		(11 , 'Noviembre'),
		(12 , 'Diciembre'),
	)

	partida = models.ForeignKey(Partida)
	mes = models.IntegerField(choices=Mes_CHOICES)
	monto_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	def __str__(self):
		return '{} {}'.format(self.partida, self.mes)
from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.db.models import Sum

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

class Capitulo(models.Model):
	programa = models.ForeignKey(Programa)
	codigo = models.CharField(max_length=4)
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{} {}'.format(self.codigo, self.nombre)

class Partida(models.Model):
	capitulo = models.ForeignKey(Capitulo)
	codigo = models.IntegerField()
	descripcion = models.TextField()	
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	def MontoAnualAutorizado(self):
		total_monto_autorizado_dict = Mes.objects.aggregate(Sum('monto_autorizado'))
		self.monto_anual_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		#self.monto_anual_autorizado
		self.save()

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
	monto_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	
	def MontoModificado(self):
		self.monto_modificado = self.monto_autorizado + self.monto_ampliacion - self.monto_reduccion
		self.save()

	def MontoPorEjercer(self):
		self.monto_por_ejercer = self.monto_modificado - self.monto_ejercido
		self.save()

	def __str__(self):
		return '{} {}'.format(self.partida, self.mes)

##		self.published_date = timezone.now()
#		self.save()
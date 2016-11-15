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
	monto = models.DecimalField(max_digits=20,decimal_places=2)
	#partida = models.IntegerField(choices=Partida_CHOICES, blank=True, null=True)
	def __str__(self):
		return self.nombre

class Partida(models.Model):
	Capitulo_CHOICES = (
		(1000 , '1000 - Servicios personales'),
		(2000 , '2000 - Materiales y suministros'),
		(3000 , '3000 - Servicios generales'),
		(4000 , '4000 - Servicios generales'),
	)
	programa = models.ForeignKey(Programa)
	capitulo = models.IntegerField(null=True, blank=True, choices=Capitulo_CHOICES)
	codigo = models.IntegerField()
	descripcion = models.TextField()	
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2)

	monto_enero_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_enero_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_enero_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0) 
	monto_enero_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_febrero_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_febrero_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_febrero_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	
	monto_marzo_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_marzo_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_marzo_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	
	monto_abril_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_abril_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_abril_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0) 
	
	monto_mayo_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_mayo_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_mayo_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_junio_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_junio_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_junio_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_julio_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_julio_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_julio_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_agosto_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_agosto_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_agosto_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_septiembre_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_septiembre_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_septiembre_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_octubre_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_octubre_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_octubre_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_noviembre_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_noviembre_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_noviembre_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)

	monto_diciembre_autorizado = models.DecimalField(max_digits=20,decimal_places=2) 
	monto_diciembre_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_diciembre_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	def __str__(self):
		return '{} {}'.format(self.codigo, self.descripcion)


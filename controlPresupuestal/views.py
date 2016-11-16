from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.db.models import Sum

class ListViewProgramas(View):
	def get(self, request):
		template_name = "controlPresupuestal/listProgramas.html"

		programas = Programa.objects.all()

		context = {
		'programas': programas,
		}
		return render(request, template_name, context)

class DetailViewProgramas(View):
	def get(self, request, pk):
		template_name= "controlPresupuestal/listPartidas.html"

		programa = get_object_or_404(Programa, pk=pk)
		partidas = Partida.objects.filter(programa=programa).order_by('codigo')

		suma_enero_autorizado = 0
		suma_enero_ampliacion = 0
		suma_enero_reduccion = 0

		suma_febrero_autorizado = 0
		suma_febrero_ampliacion = 0
		suma_febrero_reduccion = 0

		suma_marzo_autorizado = 0
		suma_marzo_ampliacion = 0
		suma_marzo_reduccion = 0

		suma_abril_autorizado = 0
		suma_abril_ampliacion = 0
		suma_abril_reduccion = 0

		suma_mayo_autorizado = 0
		suma_mayo_ampliacion = 0
		suma_mayo_reduccion = 0

		suma_junio_autorizado = 0
		suma_junio_ampliacion = 0
		suma_junio_reduccion = 0

		suma_julio_autorizado = 0
		suma_julio_ampliacion = 0
		suma_julio_reduccion = 0

		suma_agosto_autorizado = 0
		suma_agosto_ampliacion = 0
		suma_agosto_reduccion = 0

		suma_septiembre_autorizado = 0
		suma_septiembre_ampliacion = 0
		suma_septiembre_reduccion = 0

		suma_octubre_autorizado = 0
		suma_octubre_ampliacion = 0
		suma_octubre_reduccion = 0

		suma_noviembre_autorizado = 0
		suma_noviembre_ampliacion = 0
		suma_noviembre_reduccion = 0

		suma_diciembre_autorizado = 0
		suma_diciembre_ampliacion = 0
		suma_diciembre_reduccion = 0
		suma_anual = 0

		operaciones = []
		for partida in partidas:
			suma_enero_autorizado = suma_enero_autorizado + partida.monto_enero_autorizado
			suma_enero_ampliacion = suma_enero_ampliacion + partida.monto_enero_ampliacion
			suma_enero_reduccion = suma_enero_reduccion + partida.monto_enero_reduccion

			suma_febrero_autorizado = suma_febrero_autorizado + partida.monto_febrero_autorizado
			suma_febrero_ampliacion = suma_febrero_ampliacion + partida.monto_febrero_ampliacion
			suma_febrero_reduccion = suma_febrero_reduccion + partida.monto_febrero_reduccion

			suma_marzo_autorizado = suma_marzo_autorizado + partida.monto_marzo_autorizado
			suma_marzo_ampliacion = suma_marzo_ampliacion + partida.monto_marzo_ampliacion
			suma_marzo_reduccion = suma_marzo_reduccion + partida.monto_marzo_reduccion

			suma_abril_autorizado = suma_abril_autorizado + partida.monto_abril_autorizado
			suma_abril_ampliacion = suma_abril_ampliacion + partida.monto_abril_ampliacion
			suma_abril_reduccion = suma_abril_reduccion + partida.monto_abril_reduccion

			suma_mayo_autorizado = suma_mayo_autorizado + partida.monto_mayo_autorizado
			suma_mayo_ampliacion = suma_mayo_ampliacion + partida.monto_mayo_ampliacion
			suma_mayo_reduccion = suma_mayo_reduccion + partida.monto_mayo_reduccion

			suma_junio_autorizado = suma_junio_autorizado + partida.monto_junio_autorizado
			suma_junio_ampliacion = suma_junio_ampliacion + partida.monto_junio_ampliacion
			suma_junio_reduccion = suma_junio_reduccion + partida.monto_junio_reduccion

			suma_julio_autorizado = suma_julio_autorizado + partida.monto_julio_autorizado
			suma_julio_ampliacion = suma_julio_ampliacion + partida.monto_julio_ampliacion
			suma_julio_reduccion = suma_julio_reduccion + partida.monto_julio_reduccion

			suma_agosto_autorizado = suma_agosto_autorizado + partida.monto_agosto_autorizado
			suma_agosto_ampliacion = suma_agosto_ampliacion + partida.monto_agosto_ampliacion
			suma_agosto_reduccion = suma_agosto_reduccion + partida.monto_agosto_reduccion

			suma_septiembre_autorizado = suma_septiembre_autorizado + partida.monto_septiembre_autorizado
			suma_septiembre_ampliacion = suma_septiembre_ampliacion + partida.monto_septiembre_ampliacion
			suma_septiembre_reduccion = suma_septiembre_reduccion + partida.monto_septiembre_reduccion

			suma_octubre_autorizado = suma_octubre_autorizado + partida.monto_octubre_autorizado
			suma_octubre_ampliacion = suma_octubre_ampliacion + partida.monto_octubre_ampliacion
			suma_octubre_reduccion = suma_octubre_reduccion + partida.monto_octubre_reduccion

			suma_noviembre_autorizado = suma_noviembre_autorizado + partida.monto_noviembre_autorizado
			suma_noviembre_ampliacion = suma_noviembre_ampliacion + partida.monto_noviembre_ampliacion
			suma_noviembre_reduccion = suma_noviembre_reduccion + partida.monto_noviembre_reduccion

			suma_diciembre_autorizado = suma_diciembre_autorizado + partida.monto_diciembre_autorizado
			suma_diciembre_ampliacion = suma_diciembre_ampliacion + partida.monto_diciembre_ampliacion
			suma_diciembre_reduccion = suma_diciembre_reduccion + partida.monto_diciembre_reduccion

			suma_anual = suma_anual + partida.monto_anual_autorizado

		context = {
		'programa': programa,
		'partidas': partidas,
		'suma_enero_autorizado': suma_enero_autorizado,
		'suma_enero_ampliacion': suma_enero_ampliacion,
		'suma_enero_reduccion': suma_enero_reduccion,

		'suma_febrero_autorizado': suma_febrero_autorizado,
		'suma_febrero_ampliacion': suma_febrero_ampliacion,
		'suma_febrero_reduccion': suma_febrero_reduccion,
		'suma_marzo_autorizado': suma_marzo_autorizado,
		'suma_marzo_ampliacion': suma_marzo_ampliacion,
		'suma_marzo_reduccion': suma_marzo_reduccion,
		'suma_abril_autorizado': suma_abril_autorizado,
		'suma_abril_ampliacion': suma_abril_ampliacion,
		'suma_abril_reduccion': suma_abril_reduccion,
		'suma_mayo_autorizado': suma_mayo_autorizado,
		'suma_mayo_ampliacion': suma_mayo_ampliacion,
		'suma_mayo_reduccion': suma_mayo_reduccion,
		'suma_junio_autorizado': suma_junio_autorizado,
		'suma_junio_ampliacion': suma_junio_ampliacion,
		'suma_junio_reduccion': suma_junio_reduccion,
		'suma_julio_autorizado': suma_julio_autorizado,
		'suma_julio_ampliacion': suma_julio_ampliacion,
		'suma_julio_reduccion': suma_julio_reduccion,
		'suma_agosto_autorizado': suma_agosto_autorizado,
		'suma_agosto_ampliacion': suma_agosto_ampliacion,
		'suma_agosto_reduccion': suma_agosto_reduccion,
		'suma_septiembre_autorizado': suma_septiembre_autorizado,
		'suma_septiembre_ampliacion': suma_septiembre_ampliacion,
		'suma_septiembre_reduccion': suma_septiembre_reduccion,
		'suma_octubre_autorizado': suma_octubre_autorizado,
		'suma_octubre_ampliacion': suma_octubre_ampliacion,
		'suma_octubre_reduccion': suma_octubre_reduccion,
		'suma_noviembre_autorizado': suma_noviembre_autorizado,
		'suma_noviembre_ampliacion': suma_noviembre_ampliacion,
		'suma_noviembre_reduccion': suma_noviembre_reduccion,
		'suma_diciembre_autorizado': suma_diciembre_autorizado,
		'suma_diciembre_ampliacion': suma_diciembre_ampliacion,
		'suma_diciembre_reduccion': suma_diciembre_reduccion,
		'suma_anual': suma_anual,
		}
		return render(request, template_name, context)

class CreateViewPrograma(CreateView):
	
	model = Programa
	success_url = reverse_lazy('controlPresupuestal:ListViewProgramas')
	fields = ['nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año', 'fecha_creado', 'monto']

class CreateListViewPartida(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/createPartida.html"
		programa = get_object_or_404(Programa, pk=pk)

		partidaForm = PartidaForm()
		context = {
			'programa': programa,
			'partidaForm': partidaForm
		}
		return render(request,template_name,context)
	def post(self, request, pk):
		template_name = "controlPresupuestal/createPartida.html"
		programa = get_object_or_404(Programa, pk=pk)
		nuevaPartidaForm = PartidaForm(request.POST)
		if nuevaPartidaForm.is_valid():
			nuevaPartida = nuevaPartidaForm.save(commit=False)
			nuevaPartida.programa = programa
			nuevaPartida.save()
		return redirect("controlPresupuestal:DetailViewProgramas", pk=pk)

class UpdateListViewPartida(View):
	def get

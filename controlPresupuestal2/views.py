from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListViewProgramas(View):
	def get(self, request):
		template_name = "controlPresupuestal/listProgramas.html"

		programas = Programa.objects.all()

		context = {
		'programas': programas,
		}
		return render(request, template_name, context)

class ListViewPartidas(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/listPartidas.html"

		programa = get_object_or_404(Programa, pk=pk)
		partidas = Partida.objects.filter(programa=programa).order_by('codigo')

		context = {
		'programa': programa,
		'partidas': partidas,
		}
		return render(request, template_name, context)

class ListViewMeses(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/listMeses.html"

		partida = get_object_or_404(Partida, pk=pk)
		meses = Mes.objects.filter(partida=partida).order_by('mes')

		total_monto_autorizado = 0
		total_monto_ampliacion = 0
		total_monto_reduccion = 0
		total_monto_ejercido = 0
		for mes in meses:
			total_monto_autorizado = total_monto_autorizado + mes.monto_autorizado
			total_monto_ampliacion = total_monto_ampliacion + mes.monto_ampliacion
			total_monto_reduccion = total_monto_reduccion + mes.monto_reduccion
			total_monto_ejercido = total_monto_ejercido + mes.monto_ejercido
		context = {
		'partida': partida,
		'meses': meses,
		'total_monto_autorizado': total_monto_autorizado,
		'total_monto_ampliacion': total_monto_ampliacion,
		'total_monto_reduccion': total_monto_reduccion,
		'total_monto_ejercido': total_monto_ejercido,
		}
		return render(request, template_name, context)
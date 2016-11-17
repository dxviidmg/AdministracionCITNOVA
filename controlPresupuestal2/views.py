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
		meses = Mes.objects.filter(partida=partidas)

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

		montos_por_mes = []
		total_monto_autorizado = 0
		total_monto_ampliacion = 0
		total_monto_reduccion = 0
		total_monto_ejercido = 0
		total_monto_modificado = 0
		total_monto_por_ejercer = 0
		for mes in meses:
			monto_modificado = mes.monto_autorizado + mes.monto_ampliacion - mes.monto_reduccion 
			total_monto_autorizado = total_monto_autorizado + mes.monto_autorizado
			total_monto_ampliacion = total_monto_ampliacion + mes.monto_ampliacion
			total_monto_reduccion = total_monto_reduccion + mes.monto_reduccion
			total_monto_ejercido = total_monto_ejercido + mes.monto_ejercido
			total_monto_modificado = total_monto_modificado + mes.monto_modificado
			total_monto_por_ejercer = total_monto_por_ejercer + mes.monto_por_ejercer
		
		context = {
		'partida': partida,
		'meses': meses,
		'total_monto_autorizado': total_monto_autorizado,
		'total_monto_ampliacion': total_monto_ampliacion,
		'total_monto_reduccion': total_monto_reduccion,
		'total_monto_ejercido': total_monto_ejercido,
		'total_monto_modificado': total_monto_modificado,
		'total_monto_por_ejercer': total_monto_por_ejercer,
		}
		return render(request, template_name, context)
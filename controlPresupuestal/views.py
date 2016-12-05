from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.db.models import Sum
#from querysetjoin import QuerySetJoin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy 

class ListViewProgramas(View):
	def get(self, request):
		template_name = "controlPresupuestal/listProgramas.html"

		programas = Programa.objects.all()

		context = {
		'programas': programas,
		}
		return render(request, template_name, context)

class ListViewCapitulos(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/listCapitulos.html"
		programa = get_object_or_404(Programa, pk=pk)
		capitulos = Capitulo.objects.filter(programa=programa)

		context = {
		'programa': programa,
		'capitulos': capitulos,
		}
		return render(request, template_name, context)

class ListViewPartidas(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/listPartidas.html"

		capitulo = get_object_or_404(Capitulo, pk=pk)
		partidas = Partida.objects.filter(capitulo=capitulo).order_by('codigo')
		meses_de_todas_las_partida = Mes.objects.filter(partida__in=partidas)
		
		context = {
		'capitulo': capitulo,
		'partidas': partidas,
		'meses_de_todas_las_partida': meses_de_todas_las_partida,
		}
		return render(request, template_name, context)

class ListViewMeses(View):
	def get(self, request, pk):
		template_name = "controlPresupuestal/listMeses.html"

		partida = get_object_or_404(Partida, pk=pk)
		meses = Mes.objects.filter(partida=partida).order_by('mes')
		
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_autorizado'))
		total_monto_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']

		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ampliacion'))
		total_monto_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']

		total_monto_reduccion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_reduccion'))
		total_monto_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']

		total_monto_modificado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_modificado'))
		total_monto_modificado = total_monto_modificado_dict['monto_modificado__sum']

		total_monto_ejercido_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ejercido'))
		total_monto_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']

		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_por_ejercer'))
		total_monto_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		
		context = {
		'partida': partida,
		'meses': meses,
		'total_monto_autorizado': total_monto_autorizado,
		'total_monto_ampliacion': total_monto_ampliacion,
		'total_monto_reduccion': total_monto_reduccion,
		'total_monto_modificado': total_monto_modificado,
		'total_monto_ejercido': total_monto_ejercido,
		'total_monto_por_ejercer': total_monto_por_ejercer,
		}
		return render(request, template_name, context)


	
class CreateViewPrograma(CreateView):
	model = Programa
	success_url = reverse_lazy('controlPresupuestal:ListViewProgramas')
	fields = ['nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año']

class UpdateViewPrograma(UpdateView):
	model = Programa
	success_url = reverse_lazy('controlPresupuestal:ListViewProgramas')
	fields = ['nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año',]

class DeleteViewPrograma(DeleteView):
	model = Programa
	success_url = reverse_lazy('controlPresupuestal:ListViewProgramas')
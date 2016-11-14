from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *

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
		partidas = Partida.objects.filter(programa=programa)
		context = {
		'programa': programa,
		'partidas': partidas,
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


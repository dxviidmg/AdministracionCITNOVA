from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *
from django.db.models import Count
from accounts.models import *
from django.contrib.auth.models import User

class ListViewMisSolicitudes(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "recursosFinancieros/ListViewMisSolicitudes.html"
		
		#todos = User.objects.all()
		solicitudes = SolicitudRecursoFinanciero.objects.filter(solicitante=request.user)
		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

class CreateViewSolicitudPropia(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "recursosFinancieros/createSolicitudPropia.html"
		
		solicitudes = SolicitudRecursoFinanciero.objects.filter(solicitante=request.user).count()
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)
		departamento = Departamento.objects.get(perfil=perfil)
		SolicitudRecursoFinancieroForn = SolicitudRecursoFinancieroPropioCreateForm()
		context = {
			'solicitudes': solicitudes,
			'SolicitudRecursoFinancieroForn': SolicitudRecursoFinancieroForn,
			'user': user,
			'perfil': perfil,
			'departamento': departamento,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "recursosFinancieros/createSolicitudPropia.html"

		solicitudActual = SolicitudRecursoFinanciero.objects.filter(solicitante=request.user).count() + 1

		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)
		departamento = Departamento.objects.get(perfil=perfil)

		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroPropioCreateForm(request.POST)
		
		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = str(departamento.codigo) + str(solicitudActual)
			NuevoSolicitudRecursoFinanciero.a_nombre_de = str(user.first_name) + " " + str(user.last_name)
			NuevoSolicitudRecursoFinanciero.clabe = str(perfil.cta_bancaria) 
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("recursosFinancieros:ListViewMisSolicitudes")

class CreateViewSolicitudEmpleado(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "recursosFinancieros/createSolicitudEmpleado.html"
		
		solicitudes = SolicitudRecursoFinanciero.objects.filter(solicitante=request.user).count()
#		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=request.user)
		departamento = Departamento.objects.get(perfil=perfil)
		users = User.objects.all().exclude(pk=request.user.pk)

		SolicitudRecursoFinancieroForn = SolicitudRecursoFinancieroEmpleadoCreateForm(departamento=departamento)
		context = {
			'solicitudes': solicitudes,
			'SolicitudRecursoFinancieroForn': SolicitudRecursoFinancieroForn,
			#'user': user,
			'perfil': perfil,
			'departamento': departamento,
			#'empleados': empleados,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "recursosFinancieros/createSolicitudEmpleado.html"

		solicitudActual = SolicitudRecursoFinanciero.objects.filter(solicitante=request.user).count() + 1

		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)
		departamento = Departamento.objects.get(perfil=perfil)

		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroEmpleadoCreateForm(request.POST)
		
		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = str(departamento.codigo) + str(solicitudActual)
			NuevoSolicitudRecursoFinanciero.a_nombre_de = str(user.first_name) + " " + str(user.last_name)
			NuevoSolicitudRecursoFinanciero.clabe = str(perfil.cta_bancaria) 
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("recursosFinancieros:ListViewMisSolicitudes")
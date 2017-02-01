from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.db.models import Count

class ListViewTodos(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewTodos.html"
		
		#todos = User.objects.all()
		todos = User.objects.filter(is_staff=False)
		context = {
			'todos': todos,
		}
		return render(request,template_name,context)

class CreateViewEmpleado(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createEmpleado.html"
		
		UserForm = UserCreateForm()
		PerfilEmpleadoForm = PerfilEmpleadoCreateForm()
		
		context = {
			'UserForm': UserForm,
			'PerfilEmpleadoForm': PerfilEmpleadoForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createEmpleado.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserCreateForm(request.POST)
		NuevoPerfilForm = PerfilEmpleadoCreateForm(request.POST)
		
		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = 'EMP' + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.last_name[1].upper()) + str(userActual)
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
		return redirect("accounts:ListViewTodos")

class CreateViewProveedor(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createProveedor.html"
		
		UserForm = UserCreateForm()
		PerfilProveedorForm = PerfilProveedorCreateForm()
		
		context = {
			'UserForm': UserForm,
			'PerfilProveedorForm': PerfilProveedorForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createProveedor.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserCreateForm(request.POST)
		NuevoPerfilForm = PerfilProveedorCreateForm(request.POST)
		
		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = 'PROV' + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.last_name[1].upper()) + str(userActual)
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
		return redirect("accounts:ListViewTodos")

class profile(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		
		context = {
		}
		return render(request,template_name,context)
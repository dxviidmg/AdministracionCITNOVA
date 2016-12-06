from django.conf.urls import url
from . import views


urlpatterns = [
#	
	url(r'^programas/nuevo/$', views.CreateViewPrograma.as_view(), name="CreateViewPrograma"),
	url(r'^programas/actualizar/(?P<pk>\d+)/$', views.UpdateViewPrograma.as_view(), name="UpdateViewPrograma"),
	url(r'^programas/eliminar/(?P<pk>\d+)/$', views.DeleteViewPrograma.as_view(), name="DeleteViewPrograma"),
	

	url(r'^programas/capitulos/partidas/meses/nuevo/(?P<pk>\d+)/$', views.CreateViewMes.as_view(), name="CreateViewMes"),
	url(r'^programas/capitulos/partidas/meses/actualizar/(?P<pk>\d+)/$', views.UpdateViewMes.as_view(), name="UpdateViewMes"),
	url(r'^programas/capitulos/partidas/meses/eliminar/(?P<pk>\d+)/$', views.DeleteViewMes.as_view(), name="DeleteViewMes"),
	url(r'^programas/capitulos/partidas/meses/(?P<pk>\d+)/$', views.ListViewMeses.as_view(), name="ListViewMeses"),

	url(r'^programas/capitulos/partidas/nuevo/(?P<pk>\d+)/$', views.CreateViewPartida.as_view(), name="CreateViewPartida"),
	url(r'^programas/capitulos/partidas/actualizar/(?P<pk>\d+)/$', views.UpdateViewPartida.as_view(), name="UpdateViewPartida"),
	url(r'^programas/capitulos/partidas/eliminar/(?P<pk>\d+)/$', views.DeleteViewPartida.as_view(), name="DeleteViewPartida"),
	url(r'^programas/capitulos/partidas/(?P<pk>\d+)/$', views.ListViewPartidas.as_view(), name="ListViewPartidas"),

	url(r'^programas/capitulos/(?P<pk>\d+)/$', views.ListViewCapitulos.as_view(), name="ListViewCapitulos"),
	url(r'^programas',views.ListViewProgramas.as_view(),name='ListViewProgramas'),

]
from django.conf.urls import url
from . import views


urlpatterns = [
#	
	url(r'^programas/nuevo/$', views.CreateViewPrograma.as_view(), name="CreateViewPrograma"),
	url(r'^programas/actualizar/(?P<pk>\d+)/$', views.UpdateViewPrograma.as_view(), name="UpdateViewPrograma"),
	url(r'^programas/eliminar/(?P<pk>\d+)/$', views.DeleteViewPrograma.as_view(), name="DeleteViewPrograma"),
	url(r'^programas/capitulos/partidas/meses/(?P<pk>\d+)/$', views.ListViewMeses.as_view(), name="ListViewMeses"),
	url(r'^programas/capitulos/partidas/(?P<pk>\d+)/$', views.ListViewPartidas.as_view(), name="ListViewPartidas"),
	url(r'^programas/capitulos/(?P<pk>\d+)/$', views.ListViewCapitulos.as_view(), name="ListViewCapitulos"),
	url(r'^programas',views.ListViewProgramas.as_view(),name='ListViewProgramas'),

]
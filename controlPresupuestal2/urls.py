from django.conf.urls import url
from . import views


urlpatterns = [
#	url(r'^programas/partidas/(?P<pk>\d+)/$', views.UpdateListViewPartida.as_view(), name="UpdateListViewPartida"),
#	url(r'^programas/(?P<pk>\d+)/partidas//nuevo/$', views.CreateListViewPartida.as_view(), name="CreateListViewPartida"),
#	url(r'^programas/nuevo/$', views.CreateViewPrograma.as_view(), name="CreateViewPrograma"),
	url(r'^capitulos/partidas/meses/(?P<pk>\d+)/$', views.ListViewMeses.as_view(), name="ListViewMeses"),
	url(r'^capitulos/partidas/(?P<pk>\d+)/$', views.ListViewPartidas.as_view(), name="ListViewPartidas"),
	url(r'^capitulos/(?P<pk>\d+)/$', views.ListViewCapitulos.as_view(), name="ListViewCapitulos"),
	url(r'^',views.ListViewProgramas.as_view(),name='ListViewProgramas'),
]
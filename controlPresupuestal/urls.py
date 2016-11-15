from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^programas/partidas/(?P<pk>\d+)/$', views.UpdateListViewPartida.as_view(), name="UpdateListViewPartida"),
	url(r'^programas/(?P<pk>\d+)/partidas//nuevo/$', views.CreateListViewPartida.as_view(), name="CreateListViewPartida"),
	url(r'^programas/nuevo/$', views.CreateViewPrograma.as_view(), name="CreateViewPrograma"),
	url(r'^programas/$',views.ListViewProgramas.as_view(),name='ListViewProgramas'),
	url(r"^programas/(?P<pk>\d+)/$", views.DetailViewProgramas.as_view(), name="DetailViewProgramas"),
]
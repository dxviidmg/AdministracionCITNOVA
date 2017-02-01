from django.conf.urls import url
from . import views

urlpatterns = [
#	url(r'^accounts/empleado/nuevo/$',views.CreateViewEmpleado.as_view(), name='CreateViewEmpleado'),
#	url(r'^accounts/proveedor/nuevo/$',views.CreateViewProveedor.as_view(), name='CreateViewProveedor'),
	url(r'^solicitudes/nueva/propia/$',views.CreateViewSolicitudPropia.as_view(), name='CreateViewSolicitudPropia'),
	url(r'^solicitudes/nueva/empleado/$',views.CreateViewSolicitudEmpleado.as_view(), name='CreateViewSolicitudEmpleado'),
	url(r'^solicitudes/$',views.ListViewMisSolicitudes.as_view(), name='ListViewMisSolicitudes'),
]
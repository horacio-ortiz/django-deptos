from django.conf.urls import url
from django.urls import path, re_path
from departamentos import views
from departamentos.views import listaDeptoView

urlpatterns = [
    path('departamento/', views.DeptoView.as_view(), name='depto'),
    path('listadepartamentos/', views.listaDeptoView.as_view(), name='listadepto'),
    #re_path(r'^editardepartamento/(?P<pk>\d+)$', views.editDeptoView.as_view(), name='editdepto'),
    re_path(r'^editardepartamento/(?P<depto_id>\d+)$', views.edit_Depto, name='editdepto'),
]

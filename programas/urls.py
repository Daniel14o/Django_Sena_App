from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.listado_programas, name='programas_lista'),
    
    path('<str:codigo_programa>/', views.detalle_programa, name='programa_detalle'),
]
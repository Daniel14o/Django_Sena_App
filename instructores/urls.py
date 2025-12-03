from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la lista
    path('', views.listado_instructores, name='instructores_lista'),
    
    # Ruta del detalle
    # <str:documento_id> captura el número que viene del enlace
    path('<str:documento_id>/', views.detalle_instructor, name='instructor_detalle'),
]
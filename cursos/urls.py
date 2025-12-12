from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
   
    path('lista/', views.lista_cursos, name='lista_cursos'),
    
    path('crear/', views.crear_curso, name='crear_curso'),
    path('editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    
    path('detalle/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]
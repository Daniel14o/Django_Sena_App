from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    
    path('', views.ProgramaListView.as_view(), name='lista_programas'),
    
    path('detalle/<int:pk>/', views.ProgramaDetailView.as_view(), name='detalle_programa'),
    
    path('crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('editar/<int:pk>/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('eliminar/<int:pk>/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
]
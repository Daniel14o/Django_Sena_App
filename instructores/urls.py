from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    
    path('', views.InstructorListView.as_view(), name='lista_instructores'),
    
    path('detalle/<int:pk>/', views.InstructorDetailView.as_view(), name='detalle_instructor'),
    
    path('crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),
    path('editar/<int:pk>/', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('eliminar/<int:pk>/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
]
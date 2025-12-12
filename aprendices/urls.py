from django.urls import include, path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    
    path('lista/', views.all_aprendices, name='ver_aprendices'),
    
    path('agregar/', views.agregar_aprendiz, name='agregar_aprendiz'),
    path('editar/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('eliminar/<str:documento>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
    
    path('detalles/<str:documento>/', views.details, name='details'),

    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
]
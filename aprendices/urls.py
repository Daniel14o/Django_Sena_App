from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.all_aprendices, name='all_aprendices'),
    path('detalles/<str:documento>/', views.details, name='details'),
    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
]
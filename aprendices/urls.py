from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.all_aprendices, name='all_aprendices'),
    path('detalles/<str:documento>/', views.details, name='details'),
]
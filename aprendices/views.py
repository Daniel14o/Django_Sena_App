from django.shortcuts import render, get_object_or_404
from .models import Aprendiz

def main(request):
    return render(request, 'main.html')

def all_aprendices(request):
    aprendices = Aprendiz.objects.all() # Trae los datos de SQLite
    return render(request, 'all_aprendices.html', {'aprendices': aprendices})

def details(request, documento):
    # Busca por documento, si no existe devuelve error 404
    aprendiz = get_object_or_404(Aprendiz, documento_identidad=documento)
    return render(request, 'details.html', {'aprendiz': aprendiz})
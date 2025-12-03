from django.shortcuts import render, get_object_or_404
from .models import Programa

# 1. Vista para listar todos los programas
def listado_programas(request):
    programas = Programa.objects.all()
    context = {
        'programas': programas
    }
    # Renderiza la plantilla de la lista
    return render(request, 'all_programas.html', context)

# 2. Vista para ver el detalle de un programa específico
def detalle_programa(request, codigo_programa):
    # Buscamos por el campo 'codigo' del modelo
    programa = get_object_or_404(Programa, codigo=codigo_programa)
    context = {
        'programa': programa
    }
    # Renderiza la plantilla de detalle (seguimos tu patrón de nombres)
    return render(request, 'details_programa.html', context)
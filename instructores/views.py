from django.shortcuts import render, get_object_or_404
from .models import Instructor

# Vista para listar instructores
def listado_instructores(request):
    instructores = Instructor.objects.all()
    context = {
        'instructores': instructores
    }
    return render(request, 'all_instructores.html', context)

# Vista para detalle 
def detalle_instructor(request, documento_id):
    instructor = get_object_or_404(Instructor, documento_identidad=documento_id)
    context = {
        'instructor': instructor
    }
    return render(request, 'details_instructor.html', context)
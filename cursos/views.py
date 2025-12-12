from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm


def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    return render(request, 'lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'agregar_curso.html', {'form': form})

def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista_cursos')
    else:
        form = CursoForm(instance=curso)
        
    return render(request, 'editar_curso.html', {'form': form, 'curso': curso})

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:lista_cursos')
        
    return render(request, 'eliminar_curso.html', {'curso': curso})
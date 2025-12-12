from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz
from .forms import AprendizForm 

def main(request):
    return render(request, 'main.html')

def all_aprendices(request):
    aprendices = Aprendiz.objects.all()
    return render(request, 'all_aprendices.html', {'aprendices': aprendices})

def details(request, documento):
    aprendiz = get_object_or_404(Aprendiz, documento_identidad=documento)
    return render(request, 'details.html', {'aprendiz': aprendiz})

# --- FUNCIONES NUEVAS PARA EL CRUD ---

def agregar_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aprendices:ver_aprendices')
    else:
        form = AprendizForm()
    
    return render(request, 'agregar_aprendiz.html', {'form': form})

def editar_aprendiz(request, documento):
    # Buscamos el aprendiz por su documento
    aprendiz = get_object_or_404(Aprendiz, documento_identidad=documento)
    
    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            return redirect('aprendices:ver_aprendices')
    else:
        # Pre-llenamos el formulario con los datos actuales
        form = AprendizForm(instance=aprendiz)
        
    return render(request, 'editar_aprendiz.html', {'form': form, 'aprendiz': aprendiz})

def eliminar_aprendiz(request, documento):
    aprendiz = get_object_or_404(Aprendiz, documento_identidad=documento)
    
    if request.method == 'POST':
        aprendiz.delete()
        return redirect('aprendices:ver_aprendices')
        
    return render(request, 'eliminar_aprendiz.html', {'aprendiz': aprendiz})
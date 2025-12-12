from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm 

# 1. LISTAR
class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructores/all_instructores.html' # Ruta corregida
    context_object_name = 'instructores'

# 2. DETALLE
class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructores/details_instructor.html' # Ruta corregida
    context_object_name = 'instructor'

# 3. CREAR
class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'instructores/agregar_instructor.html' # Nombre estandarizado
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(self.request, f'Instructor registrado exitosamente.')
        return super().form_valid(form)

# 4. EDITAR
class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'instructores/modificar_instructor.html' # Nombre estandarizado
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(self.request, f'Instructor actualizado exitosamente.')
        return super().form_valid(form)

# 5. ELIMINAR
class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'instructores/eliminar_instructor.html' # Nombre estandarizado
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Instructor eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
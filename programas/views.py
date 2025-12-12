from django.shortcuts import render, get_object_or_404
from .models import Programa
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Programa
from .forms import ProgramaForm


class ProgramaListView(ListView):
    model = Programa
    template_name = 'programas/all_programas.html' 
    context_object_name = 'programas'


class ProgramaDetailView(DetailView):
    model = Programa
    template_name = 'programas/details_programa.html' 
    context_object_name = 'programa'


class ProgramaCreateView(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'programas/agregar_programa.html' 
    success_url = reverse_lazy('programas:lista_programas')


class ProgramaUpdateView(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'programas/editar_programa.html' 
    success_url = reverse_lazy('programas:lista_programas')


class ProgramaDeleteView(DeleteView):
    model = Programa
    template_name = 'programas/eliminar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
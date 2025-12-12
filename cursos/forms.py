from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        exclude = ['fecha_registro', 'instructores', 'aprendices']
        
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código único'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Lunes a Viernes 8-12'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'programa': forms.Select(attrs={'class': 'form-select'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-select'}),
        }
        
        labels = {
            'instructor_coordinador': 'Instructor Líder',
            'cupos_maximos': 'Cupos'
        }
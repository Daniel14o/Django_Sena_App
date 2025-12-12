from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    """Formulario para la gestión de Programas de Formación"""

    class Meta:
        model = Programa
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad',
            'duracion_meses', 'duracion_horas', 'descripcion',
            'competencias', 'perfil_egreso', 'requisitos_ingreso',
            'centro_formacion', 'regional', 'estado', 'fecha_creacion'
        ]
        
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 228106'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Análisis y Desarrollo de Software'}),
            
            # Selectores para campos con opciones (Choices)
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            
            # Campos numéricos
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            
            # Áreas de texto para descripciones largas (rows define la altura inicial)
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve descripción...'}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control'}),
            'regional': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Selector de fecha
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Validaciones personalizadas

    def clean_duracion_meses(self):
        meses = self.cleaned_data.get('duracion_meses')
        if meses is not None and meses <= 0:
            raise forms.ValidationError("La duración en meses debe ser mayor a 0.")
        return meses

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        # Ejemplo: Validar que el código no tenga espacios
        if ' ' in codigo:
            raise forms.ValidationError("El código no debe contener espacios.")
        return codigo
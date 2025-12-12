from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = '__all__'
        
        widgets = {
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1052333444'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_de_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'programa': forms.TextInput(attrs={'class': 'form-control'}),
        }
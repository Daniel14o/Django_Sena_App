from django.db import models

class Aprendiz (models.Model):

    documento_identidad = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10, null=True)
    correo_electronico = models.EmailField(null=True)
    fecha_de_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=20, null=True)
    programa = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

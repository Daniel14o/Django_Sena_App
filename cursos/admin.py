from django.contrib import admin
from cursos.models import Curso
from.models import Curso
from.models import InstructorCurso
from.models import AprendizCurso


# Register your models here.
admin.site.register(Curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)
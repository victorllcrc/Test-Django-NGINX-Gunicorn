from django.contrib import admin
from .models import anio_academico, alumno, grado ,institucion, curso, matricula

class alumno_dis (admin.ModelAdmin):
    list_display = ["nombre", "apellido"]
    class Meta:
        model1 = alumno

class anio_academico_dis (admin.ModelAdmin):
    list_display = ["nombre"]
    class Meta:
        model1 = anio_academico
class curso_dis (admin.ModelAdmin):
    list_display = ["asignatura"]
    class Meta:
        model1 = curso

class grado_dis (admin.ModelAdmin):
    list_display = ["nombre"]
    class Meta:
        model1 = grado

class institucion_dis (admin.ModelAdmin):
    list_display = ["nombre","region"]
    class Meta:
        model1 = institucion

class matricula_dis (admin.ModelAdmin):
    list_display = ["id", "alumno", "institucion"]
    class Meta:
        modell = matricula

# Register your models here.
admin.site.register(anio_academico, anio_academico_dis)
admin.site.register(alumno, alumno_dis)
admin.site.register(grado, grado_dis)
admin.site.register(institucion, institucion_dis)
admin.site.register(curso, curso_dis)
admin.site.register(matricula, matricula_dis)

from django.db import models
from tercero.models import matricula, curso
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email # me devuelve el valor por busqueda en el admin, pero se puede cambiar por otro campo... genial !!!!


class Maricula(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    ano_escola = models.CharField(max_length=4)
    inst_edu = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    nota_num = models.CharField(max_length=2)
    nota_char = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_nombre (self):
        getnom = self.nombre
        return getnom

    def get_region (self):
        getreg = self.region
        return getreg

class matricula_cn(models.Model):
    matricula = models.ForeignKey(
        matricula,
        on_delete=models.CASCADE,
    )
    curso = models.ForeignKey(
        curso,
        on_delete=models.CASCADE,
    )
    nota = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(20)]
    )


    def get_matricula(self, ind):
        dato = 2
        return dato


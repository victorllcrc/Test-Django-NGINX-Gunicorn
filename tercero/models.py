from django.db import models

#Mis modelos faltantes

class anio_academico (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class alumno(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class grado (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class institucion (models.Model):
    nombre = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    provincia = models.CharField(max_length= 50)

    def __str__(self):
        return self.nombre

class curso (models.Model):
    asignatura = models.CharField(max_length=50)

    def __str__(self):
        return self.asignatura

class matricula (models.Model):
    alumno = models.ForeignKey(
        'alumno',
        on_delete=models.CASCADE,
    )
    institucion = models.ForeignKey(
        'institucion',
        on_delete=models.CASCADE,
    )
    grado = models.ForeignKey(
        'grado',
        on_delete=models.CASCADE,
    )
    anio_academico = models.ForeignKey(
        'anio_academico',
        on_delete=models.CASCADE,
    )
    anio_escolar = models.CharField(max_length=4, default="2018")



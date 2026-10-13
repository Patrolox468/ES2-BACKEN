from django.db import models


class editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    libros = models.ManyToManyField('libro', related_name='editoriales')

    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titulo
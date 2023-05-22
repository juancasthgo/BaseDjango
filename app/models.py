from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=25)    
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=25)    
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
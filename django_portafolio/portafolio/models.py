from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    #solo debe aceptar valores del 0 al 99
    rate = models.IntegerField()
    logo = models.ImageField(upload_to="tecnologias")

class RedSocial(models.Model):
    nombre = models.CharField(max_length=50)
    enlace = models.URLField()
    logo = models.ImageField(upload_to="tecnologias")

class Educacion(models.Model):
    institucion = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="educacion")
    rol = models.CharField(max_length=50)

class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    #solo debe aceptar valores del 0 al 99
    rate = models.IntegerField()
    

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia)
    imagen = models.ImageField(upload_to="proyectos")
    url = models.URLField()

class Usuario(models.Model):
    imagen= models.ImageField(upload_to="usuarios")
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    proyectos = models.ManyToManyField(Proyecto)
    rol = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    redesSociales = models.ManyToManyField(RedSocial)
    Educacion = models.ManyToManyField(Educacion)
    idiomas = models.ManyToManyField(Idioma)

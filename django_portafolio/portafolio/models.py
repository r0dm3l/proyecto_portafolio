from django.db import models
from django.db.models.fields import CharField,URLField

# Create your models here.

class Proyecto(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=300)
    imagen = URLField(blank=True)
    url = URLField(blank=True)

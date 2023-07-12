from django.db import models

# Create your models here.
class Nave(models.Model):
    marca = models.CharField()
    modelo = models.CharField()
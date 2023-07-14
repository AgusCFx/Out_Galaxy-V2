from django.db import models

"""
class Model():
    id = IntegerField()
"""
# Create your models here.
class Nave(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
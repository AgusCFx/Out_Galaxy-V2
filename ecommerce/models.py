from django.db import models

# Create your models here.
class Nave(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    TIPO_CHOICES = (
        ('Empresarial', 'Empresarial'),
        ('Deportivo', 'Deportivo'),
        ('Familiar', 'Familiar'),
        ('Utilitario','Utilitario'),
        ('Mineria', 'Mineria'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='Familiar')
    descripcion = models.TextField(max_length=200, default='')
    cant_asientos = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    # Armas
    compatible_con_armas = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    def encontrar_armas_compatibles(self):
        if self.compatible_con_armas:
            armas_compatibles = Arma.objects.filter(naves_compatibles=self)
            print("Armas compatibles con la nave {} - {}:".format(self.marca, self.modelo))
            for arma in armas_compatibles:
                print("- {} {}".format(arma.marca, arma.modelo))
        else:
            print("Esta nave no es compatible con armas.")


class Arma(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tipo_municion = models.CharField(max_length=20)
    dpm = models.FloatField()
    descripcion = models.TextField(default='')
    naves_compatibles = models.ManyToManyField('Nave', blank=True)

    def __str__(self):
        return f"{self.marca, self.modelo}"
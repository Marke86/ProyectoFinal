from django.db import models

# Create your models here.

class Proyecto(models.Model):
    Nombre=models.CharField(max_length=50)
    Codigo=models.CharField(max_length=50)
    PresupuestoBase=models.IntegerField()
    PresupuestoActualizado=models.IntegerField()
    Responsable=models.CharField(max_length=50)

class Costos(models.Model):
    Nombre=models.CharField(max_length=50)
    Codigo=models.CharField(max_length=50)
    Mes=models.DateField()
    CostoIngenieria=models.IntegerField()
    CostoMateriales=models.IntegerField()
    CostoMontaje=models.IntegerField()
    CostoInspeccion=models.IntegerField()

class Avance(models.Model):
    Mes=models.DateField()
    AvanceIngenieria=models.IntegerField()
    AvanceCompraMateriales=models.IntegerField()
    AvanceMontaje=models.IntegerField()

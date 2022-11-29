from django import forms

class ProyectoForm(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Codigo=forms.CharField(max_length=50)
    PresupuestoBase=forms.IntegerField()
    PresupuestoActualizado=forms.IntegerField()
    Responsable=forms.CharField(max_length=50)

class CostosForm(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Codigo=forms.CharField(max_length=50)
    Mes=forms.DateField()
    CostoIngenieria=forms.IntegerField()
    CostoMateriales=forms.IntegerField()
    CostoMontaje=forms.IntegerField()
    CostoInspeccion=forms.IntegerField()

class AvanceForm(forms.Form):
    Mes=forms.DateField()
    AvanceIngenieria=forms.IntegerField()
    AvanceCompraMateriales=forms.IntegerField()
    AvanceMontaje=forms.IntegerField()
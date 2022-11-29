from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
from GestorDeProyectos.forms import *

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def ProyectoRegistro(request):
    if request.method == "POST":
        ProyFormulario=ProyectoForm(request.POST)
         
        if ProyFormulario.is_valid:
            info=ProyFormulario.cleaned_data
            NombreInfo=info["Nombre"]
            Codigoinfo=info["Codigo"]
            PresupuestoBaseInfo=info["PresupuestoBase"]
            PresupuestoActualizadoInfo=info["PresupuestoActualizado"]
            ResponsableInfo=info["Responsable"]
            proyecto=Proyecto(Nombre=NombreInfo, Codigo=Codigoinfo, PresupuestoBase=PresupuestoBaseInfo, PresupuestoActualizado=PresupuestoActualizadoInfo,
            Responsable=ResponsableInfo)
            proyecto.save()
            return render(request, "inicio.html")
    
    else:
        ProyFormulario=ProyectoForm()

    return render(request,"Proyecto_Registro.html",{"ProyFormulario":ProyFormulario})
    
def CostosRegistro(request):
    if request.method == "POST":
        CostosFormulario=CostosForm(request.POST)
         
        if CostosFormulario.is_valid:
            info=CostosFormulario.cleaned_data
            NombreInfo=info["Nombre"]
            Codigoinfo=info["Codigo"]
            MesInfo=info["Mes"]
            CostoIngenieriaInfo=info["CostoIngenieria"]
            CostoMaterialesInfo=info["CostoMateriales"]
            CostoMontajeInfo=info["CostoMontaje"]

            costos=Costos(Nombre=NombreInfo, Codigo=Codigoinfo,Mes=MesInfo, CostoIngenieria=CostoIngenieriaInfo, CostoMateriales= CostoMaterialesInfo,
            CostoMontaje=CostoMontajeInfo,)
            costos.save()
            return render(request, "inicio.html")
    
    else:
        CostosFormulario=CostosForm()

    return render(request,"Costo_Registro.html",{"CostosFormulario":CostosFormulario})
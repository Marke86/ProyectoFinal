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
         
        if ProyFormulario.is_valid():
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
         
        if CostosFormulario.is_valid():
            info=CostosFormulario.cleaned_data
            NombreInfo=info["Nombre"]
            Codigoinfo=info["Codigo"]
            MesInfo=info["Mes"]
            CostoIngenieriaInfo=info["CostoIngenieria"]
            CostoMaterialesInfo=info["CostoMateriales"]
            CostoMontajeInfo=info["CostoMontaje"]
            CostoInspeccionInfo=info["CostoInspeccion"]

            #creo el objeto
            costos=Costos(Nombre=NombreInfo, Codigo=Codigoinfo,Mes=MesInfo, CostoIngenieria=CostoIngenieriaInfo, CostoMateriales= CostoMaterialesInfo,
            CostoMontaje=CostoMontajeInfo, CostoInspeccion=CostoInspeccionInfo)
            #guardo el objeto
            costos.save()
            return render(request, "inicio.html")
    
    else:
        CostosFormulario=CostosForm()

    return render(request,"Costo_Registro.html",{"CostosFormulario":CostosFormulario})

def AvanceRegistro(request):
    if request.method == "POST":
        AvanceFormulario=AvanceForm(request.POST)
         
        if AvanceFormulario.is_valid():
            info=AvanceFormulario.cleaned_data
            MesInfo=info["Mes"]
            AvanceIngenieriaInfo=info["AvanceIngenieria"]
            AvanceCompraMaterialesInfo=info["AvanceCompraMateriales"]
            AvanceMontajeInfo=info["AvanceMontaje"]

            #creo el objeto
            avances=Avance(Mes=MesInfo, AvanceIngenieria=AvanceIngenieriaInfo, AvanceCompraMateriales= AvanceCompraMaterialesInfo,
            AvanceMontaje=AvanceMontajeInfo)
            #guardo el objeto
            avances.save()
            return render(request, "inicio.html")
    
    else:
        AvanceFormulario=AvanceForm()

    return render(request,"Avance_Registro.html",{"AvanceFormulario":AvanceFormulario})

def BuscarProyecto(request):
    return render(request, "BuscarProyecto.html")

def Resultados(request):

    if request.GET["Nombre"]:   

        Nombre=request.GET["Nombre"]

        proyect=Proyecto.objects.filter(Nombre__icontains=Nombre)
        
        return render(request,"Resultados.html", {"proyect":proyect} )
    else:
        return render(request, "BuscarProyecto.html", {"mensaje":"No se han encontrado coincidencias"})
from django.urls import path
from GestorDeProyectos.views import *

urlpatterns = [
    path("ProyectoRegistro/", ProyectoRegistro, name="ProyectoRegistro"),
    path("inicio/", inicio, name="inicio"),
    path("CostosRegistro/",CostosRegistro,name="CostosRegistro"),
    path("AvanceRegistro/",AvanceRegistro,name="AvanceRegistro"),
    path("BuscarProyecto/", BuscarProyecto, name="BuscarProyecto"),
    path("Resultados/", Resultados, name="Resultados"),
]      

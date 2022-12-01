from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Proyecto)
admin.site.register(Costos)
admin.site.register(Avance)


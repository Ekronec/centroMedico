from django.contrib import admin
from .models import Atencion, Medico, Boleta, Especialidad, EspecialidadMedico, Secretaria, Paciente, PagoAtencion, User

admin.site.register(Atencion)
admin.site.register(Medico)
admin.site.register(Secretaria)

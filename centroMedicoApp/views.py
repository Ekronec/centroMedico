from django.shortcuts import render
from .models import Atencion
from django.utils import timezone

def index(request):
    return render(request, "pages/index.html")

def appointmentNew(request):
    if request.method != "POST":
        # Aquí puedes obtener otros datos necesarios para la vista
        # por ejemplo, pacientes, médicos, especialidades, etc.
        # Ejemplo:
        # pacientes = Paciente.objects.all()
        # medicos = Medico.objects.all()
        # especialidades = Especialidad.objects.all()
        
        context = {
            # Agrega los datos que necesitas en el contexto
            # por ejemplo:
            # 'pacientes': pacientes,
            # 'medicos': medicos,
            # 'especialidades': especialidades
        }
        return render(request, 'pages/appointmentNew.html', context)
    else:
        # Obtén los datos del formulario
        fecha_ate = request.POST.get("fecha_ate")
        hora_ate = request.POST.get("hora_ate")
        precio_ate = request.POST.get("precio_ate")
        bono_ate = request.POST.get("bono_ate")
        rut_cli_id = request.POST.get("rut_cli")
        rut_med_id = request.POST.get("rut_med")
        id_boleta_id = request.POST.get("id_boleta")
        rut_med1_id = request.POST.get("rut_med1")
        id_esp_id = request.POST.get("id_esp")
        
        # Crea el objeto de Atencion
        obj_atencion = Atencion.objects.create(
            fecha_ate=fecha_ate,
            hora_ate=hora_ate,
            precio_ate=precio_ate,
            bono_ate=bono_ate,
            rut_cli_id=rut_cli_id,
            rut_med_id=rut_med_id,
            id_boleta_id=id_boleta_id,
            rut_med1_id=rut_med1_id,
            id_esp_id=id_esp_id,
        )
        obj_atencion.save()
        context = {"mensaje": "OK Atencion Registrada"}
        return render(request, "pages/appointmentNew.html", context)
    
    
    




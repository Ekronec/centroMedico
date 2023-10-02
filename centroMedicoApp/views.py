from django.shortcuts import render, get_object_or_404
from .models import Atencion, Medico, Boleta, Especialidad, EspecialidadMedico, Secretaria, Paciente, PagoAtencion, User
from django.utils import timezone

def index(request):
    return render(request, "pages/index.html")


#Atencion

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
    
    
    
#Medico  
    
def medicoList(request):
    medicos = Medico.objects.all()
    context = {'medicos': medicos}
    return render(request, 'pages/medicoList.html', context)

def medico_detail(request, rut_med):
    medico = get_object_or_404(Medico, pk=rut_med)
    context = {'medico': medico}
    return render(request, 'pages/medicoDeatils.html', context)

def create_medico(request):
    if request.method == "POST":
        rut_med = request.POST["rut_med"]
        dv_med = request.POST["dv_med"]
        pnombre_med = request.POST["pnombre_med"]
        snombre_med = request.POST.get("snombre_med", "")
        apaterno_med = request.POST["apaterno_med"]
        amaterno_med = request.POST["amaterno_med"]
        fecnac_med = request.POST["fecnac_med"]
        honorario_med = request.POST["honorario_med"]
        email_med = request.POST["email_med"]
        telefono_med = request.POST["telefono_med"]
        feccont_med = request.POST["feccont_med"]
        rut_sec_id = request.POST["rut_sec"]
        email_user = request.POST["email_user"]
    
        medico = Medico.objects.create(
            rut_med=rut_med,
            dv_med=dv_med,
            pnombre_med=pnombre_med,
            snombre_med=snombre_med,
            apaterno_med=apaterno_med,
            amaterno_med=amaterno_med,
            fecnac_med=fecnac_med,
            honorario_med=honorario_med,
            email_med=email_med,
            telefono_med=telefono_med,
            feccont_med=feccont_med,
            rut_sec_id=rut_sec_id,
            email_user=email_user,
        )
        medico.save()
        context = {"mensaje": "OK Médico Registrado"}
        return render(request, "pages/medicoDetails.html", context)
    else:
        return render(request, 'pages/medicoNew.html', context)
    
    
#Secretaria
    
def create_secretaria(request):
    if request.method == "POST":
        rut_sec = request.POST["rut_sec"]
        dv_sec = request.POST["dv_sec"]
        pnom_sec = request.POST["pnom_sec"]
        snom_sec = request.POST.get("snom_sec", "")
        apaterno_sec = request.POST["apaterno_sec"]
        amaterno_sec = request.POST["amaterno_sec"]
        fecnac_sec = request.POST["fecnac_sec"]
        honorario_sec = request.POST["honorario_sec"]
        email_sec = request.POST["email_sec"]
        telefono_sec = request.POST["telefono_sec"]
        feccont_sec = request.POST["feccont_sec"]
        email_user = request.POST["email_user"]
    
        secretaria = Secretaria.objects.create(
            rut_sec=rut_sec,
            dv_sec=dv_sec,
            pnom_sec=pnom_sec,
            snom_sec=snom_sec,
            apaterno_sec=apaterno_sec,
            amaterno_sec=amaterno_sec,
            fecnac_sec=fecnac_sec,
            honorario_sec=honorario_sec,
            email_sec=email_sec,
            telefono_sec=telefono_sec,
            feccont_sec=feccont_sec,
            email_user=email_user,
        )
        secretaria.save()
        context = {"mensaje": "OK Secretaria Registrada"}
        return render(request, "pages/secretaria_detail.html", context)
    else:
        return render(request, 'pages/secretariaNew.html', context)
    
    
    




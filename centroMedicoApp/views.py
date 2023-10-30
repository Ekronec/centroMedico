from django.shortcuts import render, get_object_or_404, redirect
from .models import Atencion, Medico, Boleta, Especialidad, EspecialidadMedico, Secretaria, Paciente, PagoAtencion, UserCentro
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
import random
from django.db.models import Max
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "pages/index.html")


# Atencion

def appointment_details(request):
    try:
        atenciones = Atencion.objects.all();



        context ={
            "atenciones": atenciones,
        }

        return render(request, "pages/appointments_details.html", context)
    except:
        Atencion.DoesNotExist
        return HttpResponse(f'No exiten atenciones')

def appointmentNew(request):
    context = {}
    #medicos = Medico.objects.all()
    especialidad = Especialidad.objects.all();
    paciente_detail = Paciente.objects.all();
    medico_detail = Medico.objects.all();
    boleta_detail = Boleta.objects.all();
    
    context ={
        "especialidades":especialidad,
        "paciente_detail":paciente_detail,
        "medico_detail":medico_detail,
        "boleta_detail":boleta_detail,
    }
    if request.method == "POST":
        fecha_ate = request.POST["fecha_ate"]
        hora_ate = request.POST["hora_ate"]
        precio_ate = request.POST["precio_ate"]
        bono_ate = request.POST["bono_ate"]
        rut_med = request.POST["rut_med"]
        id_esp = request.POST["id_esp"]

        rut_cli = request.POST["rut_cli"]

        last_boleta = Boleta.objects.order_by('-id_boleta').first()

        if last_boleta:
            next_id_boleta = last_boleta.id_boleta + 1
        else:
            # Si no hay boletas en la base de datos, empieza en 1
            next_id_boleta = 1

        try:
            medico = Medico.objects.get(rut_med=rut_med)

        except Medico.DoesNotExist:
            return HttpResponse("No hay Medico con ese rut")

        try:
            # Intenta obtener un paciente con el mismo rut_cli_id
            paciente = Paciente.objects.get(rut_cli=rut_cli)

            # Si el paciente existe, actualiza sus detalles
            rut_cli=paciente,
            paciente.dv_cli = request.POST["dv_cli"]
            paciente.pnom_cli = request.POST["pnom_cli"]
            paciente.snom_cli = request.POST["snom_cli"]
            paciente.apaterno_cli = request.POST["apaterno_cli"]
            paciente.amaterno_cli = request.POST["amaterno_cli"]
            paciente.save()

            # Resto del código para crear boleta y atención
        except Paciente.DoesNotExist:
            # Si no existe, crea un nuevo paciente
            paciente = Paciente.objects.create(
                rut_cli=rut_cli,
                dv_cli=request.POST["dv_cli"],
                pnom_cli=request.POST["pnom_cli"],
                snom_cli=request.POST["snom_cli"],
                apaterno_cli=request.POST["apaterno_cli"],
                amaterno_cli=request.POST["amaterno_cli"],
            )
            paciente.save();
            

        try:
            boleta = Boleta.objects.create(
            id_boleta=next_id_boleta,
            fecha_boleta = request.POST["fecha_boleta"],
            monto_boleta = request.POST["monto_boleta"]
        )
            boleta.save()
        # Resto del código para crear atención

            boleta_id = Boleta.objects.get(id_boleta=next_id_boleta)
            esp_id = Especialidad.objects.get(id_esp=id_esp)
        
            atencion = Atencion.objects.create(
                fecha_ate=fecha_ate,
                hora_ate=hora_ate,
                precio_ate=precio_ate,
                bono_ate=bono_ate,
                rut_cli=paciente,
                rut_med=medico,
                id_boleta=boleta_id,
                id_esp=esp_id,
            )
            atencion.save()
            context = {"mensaje": "OK Atención Registrada"}
            return render(request, "pages/index.html", context)
        except IntegrityError:
        # Si falla por una restricción única, genera un nuevo ID de boleta y vuelve a intentar
            new_id_boleta = random.randint(100000, 999999)  # Genera un nuevo ID aleatorio
            return HttpResponse(f"Error: El ID de boleta  ya está en uso. Intenta con {new_id_boleta}")
    else:
        return render(request, 'pages/appointmentNew.html', context)
       
    
# Medico  
    
def medicoList(request):
    medicos = Medico.objects.all()
    context = {'medicos': medicos}
    return render(request, 'pages/medicoList.html', context)

def medicoDetails(request, rut_med):
    try:
        # Obtener el médico a partir del rut_med
        medico = Medico.objects.get(rut_med=rut_med)

        # Obtener las especialidades asociadas a este médico
        especialidades = Especialidad.objects.filter(
            especialidadmedico__rut_med=rut_med
        ).values('nom_esp')

        context = {
            'medico': medico,
            'especialidades': especialidades
        }

        return render(request, 'pages/medicoDetails.html', context)
    
    except Medico.DoesNotExist:
        # Manejar el caso en que no se encuentre el médico
        return render(request, 'pages/medicoDetails.html')

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
    

    
# Secretaria
    
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
    
    
# Boleta

def boleta_list(request):
    boletas = Boleta.objects.all()
    context = {'boletas': boletas}
    return render(request, 'pages/boleta_list.html', context)

def boleta_detail(request, id_boleta):
    boleta = get_object_or_404(Boleta, pk=id_boleta)
    context = {'boleta': boleta}
    return render(request, 'pages/boleta_details.html', context)

def create_boleta(request):
    if request.method == "POST":
        id_boleta = request.POST["id_boleta"]
        monto_boleta = request.POST["monto_boleta"]
        fecha_boleta = request.POST["fecha_boleta"]
    
        boleta = Boleta.objects.create(
            id_boleta=id_boleta,
            monto_boleta=monto_boleta,
            fecha_boleta=fecha_boleta,
        )
        boleta.save()
        context = {"mensaje": "OK Boleta Registrada"}
        return render(request, "pages/boleta_details.html", context)
    else:
        return render(request, 'pages/boleta_new.html')
    
    
    
# Pago Atencion

def pago_atencion_list(request):
    pagos_atencion = PagoAtencion.objects.all()
    context = {'pagos_atencion': pagos_atencion}
    return render(request, 'pages/pago_atencion_list.html', context)

def pago_atencion_detail(request, id_ate):
    pago_atencion = get_object_or_404(PagoAtencion, pk=id_ate)
    context = {'pago_atencion': pago_atencion}
    return render(request, 'pages/pago_atencion_details.html', context)

def create_pago_atencion(request):
    if request.method == "POST":
        id_ate = request.POST["id_ate"]
        fecha_pago = request.POST["fecha_pago"]
        monto_ate = request.POST["monto_ate"]
        monto_cancelar = request.POST["monto_cancelar"]
        observacion = request.POST["observacion"]
    
        pago_atencion = PagoAtencion.objects.create(
            id_ate=id_ate,
            fecha_pago=fecha_pago,
            monto_ate=monto_ate,
            monto_cancelar=monto_cancelar,
            observacion=observacion,
        )
        pago_atencion.save()
        context = {"mensaje": "OK Pago de Atención Registrado"}
        return render(request, "pages/pago_atencion_details.html", context)
    else:
        return render(request, 'pages/pago_atencion_new.html')
    


# Usuario

def user_list(request):
    users = UserCentro.objects.all()
    context = {'users': users}
    return render(request, 'pages/user_list.html', context)

def user_detail(request, email_user):
    user = get_object_or_404(UserCentro, pk=email_user)
    context = {'user': user}
    return render(request, 'pages/user_detail.html', context)

def create_user(request):
    if request.method == "POST":
        email_user = request.POST["email_user"]
        password_user = request.POST["password_user"]
    
        user = UserCentro.objects.create(
            email_user=email_user,
            password_user=password_user,
        )
        user.save()
        context = {"mensaje": "OK Usuario Registrado"}
        return render(request, "pages/user_detail.html", context)
    else:
        return render(request, 'pages/user_new.html')    
    
def login_view(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        password = request.POST['password']

        # Autenticar al usuario
        user = authenticate(request, rut=rut, password=password)

        if user is not None:
            login(request, user)
            # El usuario ha iniciado sesión exitosamente
            return redirect('página_de_inicio')  # Redirige a la página de inicio después del inicio de sesión
        else:
            # Las credenciales son incorrectas
            error_message = "Las credenciales son incorrectas. Inténtalo de nuevo."

    # Renderiza el formulario de inicio de sesión
    return render(request, 'login.html', {'error_message': error_message})

# Especialidad Medico

def especialidad_medico_list(request):
    especialidades_medico = EspecialidadMedico.objects.all()
    context = {'especialidades_medico': especialidades_medico}
    return render(request, 'pages/especialidad_medico_list.html', context)

def especialidad_medico_detail(request, rut_med, id_esp):
    especialidad_medico = get_object_or_404(EspecialidadMedico, rut_med=rut_med, id_esp=id_esp)
    context = {'especialidad_medico': especialidad_medico}
    return render(request, 'pages/especialidad_medico_detail.html', context)

def create_especialidad_medico(request):
    if request.method == "POST":
        rut_med = request.POST["rut_med"]
        id_esp = request.POST["id_esp"]
        fec_inic_esp = request.POST["fec_inic_esp"]
    
        especialidad_medico = EspecialidadMedico.objects.create(
            rut_med=rut_med,
            id_esp=id_esp,
            fec_inic_esp=fec_inic_esp,
        )
        especialidad_medico.save()
        context = {"mensaje": "OK Especialidad del Médico Registrada"}
        return render(request, "pages/especialidad_medico_detail.html", context)
    else:
        return render(request, 'pages/especialidad_medico_new.html') 
    
    
    
# Especialidad

def especialidad_list(request):
    especialidades = Especialidad.objects.all()
    context = {'especialidades': especialidades}
    return render(request, 'pages/especialidad_list.html', context)

def especialidad_detail(request, id_esp):
    especialidad = get_object_or_404(Especialidad, pk=id_esp)
    context = {'especialidad': especialidad}
    return render(request, 'pages/especialidad_detail.html', context)

def create_especialidad(request):
    if request.method == "POST":
        id_esp = request.POST["id_esp"]
        nom_esp = request.POST["nom_esp"]
        monto_esp = request.POST["monto_esp"]
    
        especialidad = Especialidad.objects.create(
            id_esp=id_esp,
            nom_esp=nom_esp,
            monto_esp=monto_esp,
        )
        especialidad.save()
        context = {"mensaje": "OK Especialidad Registrada"}
        return render(request, "pages/especialidad_detail.html", context)
    else:
        return render(request, 'pages/especialidad_new.html')

def get_precio(request, id_esp):
    especialidad = get_object_or_404(Especialidad, id_esp=id_esp)

    # Obtén el precio de la especialidad
    precio = especialidad.monto_esp

    # Devuelve el precio en la respuesta AJAX
    return JsonResponse({'precio': precio})


#Paciente

def paciente_list(request):
    pacientes = Paciente.objects.all()
    context = {'pacientes': pacientes}
    return render(request, 'pages/paciente_list.html', context)

def paciente_detail(request, rut_cli):
    paciente = get_object_or_404(Paciente, pk=rut_cli)
    context = {'paciente': paciente}
    return render(request, 'pages/paciente_detail.html', context)

def create_paciente(request):
    if request.method == "POST":
        rut_cli = request.POST["rut_cli"]
        dv_cli = request.POST["dv_cli"]
        pnom_cli = request.POST["pnom_cli"]
        snom_cli = request.POST.get("snom_cli", "")
        apaterno_cli = request.POST["apaterno_cli"]
        amaterno_cli = request.POST["amaterno_cli"]
        email_cli = request.POST.get("email_cli", "")
        telefono_cli = request.POST.get("telefono_cli", "")
    
        paciente = Paciente.objects.create(
            rut_cli=rut_cli,
            dv_cli=dv_cli,
            pnom_cli=pnom_cli,
            snom_cli=snom_cli,
            apaterno_cli=apaterno_cli,
            amaterno_cli=amaterno_cli,
            email_cli=email_cli,
            telefono_cli=telefono_cli,
        )
        paciente.save()
        context = {"mensaje": "OK Paciente Registrado"}
        return render(request, "pages/paciente_detail.html", context)
    else:
        return render(request, 'pages/paciente_new.html')


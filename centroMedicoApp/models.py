from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Boleta(models.Model):
    id_boleta = models.PositiveIntegerField(primary_key=True)
    monto_boleta = models.DecimalField(max_digits=20, decimal_places=0)
    fecha_boleta = models.DateField()

    def __str__(self):
        return f"{self.id_boleta}"
    

class Especialidad(models.Model):
    id_esp = models.PositiveIntegerField(primary_key=True)
    nom_esp = models.CharField(max_length=40)
    monto_esp = models.DecimalField(max_digits=8, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.nom_esp}"


class UserCentro(models.Model):
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    rut = GenericForeignKey('content_type', 'object_id')
    password = models.CharField(max_length=30, default="")

    def __str__(self):
        return str(self.rut)


class Paciente(models.Model):
    rut_cli = models.PositiveIntegerField(primary_key=True)
    dv_cli = models.CharField(max_length=1)
    pnom_cli = models.CharField(max_length=40)
    snom_cli = models.CharField(max_length=40, null=True, blank=True)
    apaterno_cli = models.CharField(max_length=40)
    amaterno_cli = models.CharField(max_length=40)
    email_cli = models.EmailField(null=True, blank=True)
    telefono_cli = models.PositiveIntegerField(null=True, blank=True)

    def nombre_paciente(self):
        return self.nombrepaciente_set.first().rut_cli.pnom_cli.apaterno_cli

    def __str__(self):
        return f"{self.pnom_cli} {self.apaterno_cli} {self.amaterno_cli}"

class PagoAtencion(models.Model):
    id_ate = models.PositiveIntegerField(primary_key=True)
    fecha_pago = models.DateField()
    monto_ate = models.DecimalField(max_digits=8, decimal_places=0)
    monto_cancelar = models.DecimalField(max_digits=8, decimal_places=0)
    observacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_ate}"

class Secretaria(models.Model):
    rut_sec = models.PositiveIntegerField(primary_key=True)
    dv_sec = models.CharField(max_length=1)
    pnom_sec = models.CharField(max_length=20)
    snom_sec = models.CharField(max_length=20, null=True, blank=True)
    apaterno_sec = models.CharField(max_length=40)
    amaterno_sec = models.CharField(max_length=20)
    fecnac_sec = models.DateField()
    honorario_sec = models.DecimalField(max_digits=20, decimal_places=0)
    email_sec = models.EmailField()
    telefono_sec = models.PositiveIntegerField()
    feccont_sec = models.DateField()

    def __str__(self):
        return f"{self.pnom_sec} {self.apaterno_sec} {self.amaterno_sec}"
    
class Medico(models.Model):
    rut_med = models.PositiveIntegerField(primary_key=True)
    dv_med = models.CharField(max_length=1)
    pnombre_med = models.CharField(max_length=20)
    snombre_med = models.CharField(max_length=20, null=True, blank=True)
    apaterno_med = models.CharField(max_length=40)
    amaterno_med = models.CharField(max_length=20)
    fecnac_med = models.DateField()
    honorario_med = models.DecimalField(max_digits=20, decimal_places=0)
    email_med = models.EmailField()
    telefono_med = models.PositiveIntegerField()
    feccont_med = models.DateField()
    rut_sec = models.ForeignKey('Secretaria', on_delete=models.CASCADE)

    def especialidad_nombre(self):
        return self.especialidadmedico_set.first().id_esp.nom_esp

    def __str__(self):
        return f"{self.pnombre_med} {self.apaterno_med} {self.amaterno_med}"
    


class EspecialidadMedico(models.Model):
    rut_med = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_esp = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fec_inic_esp = models.DateField()

    def __str__(self):
        return f"{self.rut_med} {self.id_esp}"

class Atencion(models.Model):
    id_ate = models.AutoField(primary_key=True)
    fecha_ate = models.DateField(default=timezone.now)
    hora_ate = models.TimeField(default=0)
    precio_ate = models.DecimalField(max_digits=20, decimal_places=0)
    bono_ate = models.CharField(max_length=20, default=0)
    rut_cli = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    rut_med = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='atenciones')
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    id_esp = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    class Meta:
        unique_together = [('id_ate', 'id_esp')]
        
    def hora_formateada(self):
        # Formatear la hora en el formato deseado (por ejemplo, 03:30 PM)
        return self.hora_ate.strftime("%I:%M %p")

    def __str__(self):
        return f"{self.fecha_ate} {self.hora_ate} {self.rut_cli}"

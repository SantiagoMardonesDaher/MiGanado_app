from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    ]

    nombre = models.CharField(max_length=100)
    nombreCampo = models.CharField(max_length=100)
    correoElectronico = models.EmailField()
    contrasenia = models.CharField(max_length=100)
    idTipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    configNotificaciones = models.OneToOneField('ConfigNotificaciones', on_delete=models.CASCADE, null=True, blank=True)
    lotes = models.ManyToManyField('Lote', blank=True)
    notificaciones = models.ManyToManyField('Notificacion', blank=True)

class Lote(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    capacidadMax = models.IntegerField()
    idTipoAnimal = models.IntegerField()
    Animales = models.ManyToManyField('Animal')

class Animal(models.Model):
    numeroCaravana = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    HistorialMedico = models.ForeignKey('HistorialMedico', on_delete=models.CASCADE)

class HistorialMedico(models.Model):
    peso = models.FloatField()
    fechaNacimiento = models.DateField()
    fechaFallecimiento = models.DateField(null=True, blank=True)
    preniada = models.BooleanField()
    tratamientos = models.ManyToManyField('Tratamiento')
    sangrado = models.ManyToManyField('Sangrado')

class Tratamiento(models.Model):
    TIPO_CHOICES = [
        ('tratamiento', 'Tratamiento'),
        ('vacunacion', 'Vacunación'),
    ]

    numeroAnimal = models.IntegerField()
    nombre = models.CharField(max_length=100)
    medicacion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    duracion = models.IntegerField()
    repeticion = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

class Sangrado(models.Model):
    numeroLote = models.IntegerField()
    numeroAnimal = models.IntegerField()
    numeroTubo = models.IntegerField()
    fecha = models.DateField()

class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('lote', 'Lote'),
        ('tratamiento', 'Tratamiento'),
        ('tacto', 'Tacto'),
        ('sangrado', 'Sangrado'),
        ('estadisticas', 'Estadísticas'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Añade la relación de usuario
    IdTipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensaje = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)  # auto_now_add para la fecha de creación

    def __str__(self):
        return f"{self.get_IdTipo_display()} - {self.mensaje}"

class ConfigNotificaciones(models.Model):
    usuario_config = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    recibir_notificaciones_lote = models.BooleanField(default=False)
    recibir_notificaciones_tratamiento = models.BooleanField(default=False)
    recibir_notificaciones_tacto = models.BooleanField(default=False)
    recibir_notificaciones_sangrado = models.BooleanField(default=False)
    recibir_notificaciones_estadisticas = models.BooleanField(default=False)

    def __str__(self):
        return f"Preferencias de notificación para {self.usuario_config.username}"


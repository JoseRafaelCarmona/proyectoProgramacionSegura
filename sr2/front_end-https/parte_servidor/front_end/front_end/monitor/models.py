from django.db import models

# Create your models here.

class usuario_logueado(models.Model):
    nombreUsuario =  models.CharField(max_length=30,null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False)

class relacion_user_servidor(models.Model):
    nombreUsuario =  models.CharField(max_length=30,null=False, blank=False)
    ip_servidor = models.CharField(max_length=16,null=False, blank=False)
    mac = models.CharField(max_length=18, null=False, blank=False)
    hostname = models.CharField(max_length=30, null=False, blank=False)
    usuario_api = models.CharField(max_length=18, null=False, blank=False, default=0)
    password_api = models.CharField(max_length=15, null=False, blank=False, default=0)
    estatus = models.BooleanField(null=False, blank=False, default=0)

class user_telegram(models.Model):
    nombreUsuario =  models.CharField(max_length=30,null=False, blank=False)
    tokenTelegram = models.CharField(max_length=50,null=False, blank=False)
    telegram = models.CharField(max_length=20,null=False, blank=False)

class IPs(models.Model):
    ip = models.GenericIPAddressField(null=False, blank=False, unique=True)
    ultima_peticion = models.DateTimeField(null=False, blank=False)
    intentos = models.IntegerField(null=False, blank=False, default=0)

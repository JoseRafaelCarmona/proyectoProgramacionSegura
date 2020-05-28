from django.db import models

# Create your models here.
class servidores(models.Model):
	mac = models.CharField(max_length=18, null=False, blank=False)
	ip = models.CharField(max_length=18, null=False, blank=False)
	hostname = models.CharField(max_length=30, null=False, blank=False)
	estado = models.CharField(max_length=30, null=False, blank=False)
	token = models.CharField(max_length=70, null=False, blank=False)

class administradores(models.Model):
	nombreAdmin = models.CharField(max_length=30,null=False, blank=False)
	nombreUsuario = models.CharField(max_length=30,null=False, blank=False)
	password = models.CharField(max_length=50,null=False, blank=False)
	ip_servidor = models.CharField(max_length=16,null=False, blank=False)
	tokenTelegram = models.CharField(max_length=50,null=False, blank=False)
	telegram = models.CharField(max_length=20,null=False, blank=False)
    
class IPs(models.Model):
    ip = models.GenericIPAddressField(null=False, blank=False, unique=True)
    ultima_peticion = models.DateTimeField(null=False, blank=False)
    intentos = models.IntegerField(null=False, blank=False, default=0)
	
	
	
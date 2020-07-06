from django.db import models

# Create your models here.

class servidor(models.Model):
    memoria_ram = models.CharField(max_length=5,default='0')
    memoria_swap = models.CharField(max_length=5,default='0')
    espacio_disco = models.CharField(max_length=5,default='0')
    numero_procesadores = models.CharField(max_length=1,default='0')

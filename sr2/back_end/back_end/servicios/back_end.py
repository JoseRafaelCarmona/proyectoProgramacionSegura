import logging
from .models import servidor
import json
import psutil
from subprocess import Popen, PIPE, STDOUT
from servicios import models
import multiprocessing

logger = logging.getLogger('servidor')
logger.setLevel(logging.DEBUG)

def registrar_datos_servidor():
    instancia = models.servidor(id="1")
    instancia.memoria_ram = calcular_memoria_ram()
    instancia.memoria_swap = calcular_swap()
    instancia.espacio_disco = calcular_espacio_disco()
    instancia.numero_procesadores = obtener_cpu()
    instancia.save()

def salidaComando():
	event = Popen('df -l | grep "/dev/sda*"', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	output = event.communicate()
	salida = output[0].decode('utf-8')
	return salida

def calcular_memoria_ram():
    memoriaRamTotal = psutil.virtual_memory()[0]
    memoriaRamOcupada = psutil.virtual_memory()[3]
    return str((memoriaRamOcupada*100)/memoriaRamTotal)[:4]

def calcular_swap():
    memoriaSwapTotal = psutil.swap_memory()[0]
    memoriaSwapOcupada = psutil.swap_memory()[1]
    return str((memoriaSwapOcupada*100)/memoriaSwapTotal)[:4]

def obtener_particiones_disco():
    particiones = salidaComando()
    particiones = particiones.split('\n')
    return particiones

def obtener_cpu():
    return multiprocessing.cpu_count()

def calcular_espacio_disco():
    listaParticiones = obtener_particiones_disco()
    listaParticiones.pop(len(listaParticiones)-1)
    discoTotal = 0
    for particion in listaParticiones:
        verificar_particion = particion.split()
        if verificar_particion[0] != "df:":
            print(particion)
            montaje = particion.split()
            disco = ((psutil.disk_usage(montaje[5])[1])*100)/psutil.disk_usage(montaje[5])[0]
            discoTotal = discoTotal + disco
    return str(discoTotal)[:4]

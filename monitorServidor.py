#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 06:55:55 2020

@author: josrall
"""

import psutil
from subprocess import Popen, PIPE, STDOUT

def salidaComando(comando):
	event = Popen(comando, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
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
    return str((memoriaSwapOcupada*100)/memoriaSwapTotal)

def obtener_particiones_disco():
    particiones = salidaComando('df -l | grep "/dev/sda*"')
    particiones = particiones.split('\n')
    return particiones

def calcular_espacio_disco():
    listaParticiones = obtener_particiones_disco()
    listaParticiones.pop(len(listaParticiones)-1)
    discoTotal = 0
    for particion in listaParticiones:
        montaje = particion.split()
        disco = ((psutil.disk_usage(montaje[5])[1])*100)/psutil.disk_usage(montaje[5])[0]
        discoTotal = discoTotal + disco
    return str(discoTotal)[:4]
        
if __name__=="__main__":
    print("Memoria Ram ocupada {0}%".format(calcular_memoria_ram()))
    print("Memoria Swap ocupada {0}%".format(calcular_swap()))
    print("Espacio en disco {0}%".format(calcular_espacio_disco()))
    

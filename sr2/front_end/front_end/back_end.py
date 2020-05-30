#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:30:23 2020

@author: josrall
"""

from monitor import models
import datetime
import subprocess
import random
import front_end.settings as settings
from django.core.cache import cache
import re
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def dejar_pasar_peticion_login(request):
    ip = get_client_ip(request)
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    try:
        registro = models.IPs.objects.get(ip=ip)
    except: # la ip nunca ha hecho peticiones
        nuevoRegistroIP = models.IPs(ip=ip, ultima_peticion=timestamp, intentos=1)
        nuevoRegistroIP.save()
        return True
    diferencia = (timestamp - registro.ultima_peticion).seconds
    if diferencia > settings.VENTANA_TIEMPO_INTENTOS_LOGIN:
        registro.ultima_peticion = timestamp
        registro.intentos=1
        registro.save()
        return True
    elif settings.INTENTOS_LOGIN > registro.intentos:
        registro.ultima_peticion = timestamp
        registro.intentos = registro.intentos+1
        registro.save()
        return True
    else:
        registro.ultima_peticion = timestamp
        registro.intentos = registro.intentos+1
        registro.save()
        return False
    
def mandar_codigo(request):
    datos = models.administradores.objects.get(nombreUsuario=request.session['usuario'])
    if obtener_Codigo(request) is not None and obtener_Codigo(request) != request.session['codigo']:
        url = 'https://api.telegram.org/bot{0}/sendMessage'.format(datos.tokenTelegram)
        mensaje = "Su codigo de verificacion es: {0}".format(request.session['codigo'])
        subprocess.call('curl -s --max-time 5 -d "chat_id={0}&disable_web_page_preview=1&text={1}" {2} >/dev/null'.format(datos.telegram,mensaje,url),shell=True)

def obtener_Codigo(request):
    if validar_token(request):
        numero = random.random()
        numero = str(numero).split('.')
        return numero[1][:6]
    else:
        return None

def validar_token(request):
    ip = get_client_ip(request)
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    datos = models.IPs.objects.get(ip=ip)
    hora_Ultima_Peticion = str(datos.ultima_peticion).split(':')
    hora_U = hora_Ultima_Peticion[0].split(' ')
    peticion_Actual = str(timestamp).split(':')
    hora_PA = peticion_Actual[0].split(' ')
    if hora_PA[1] == hora_U[1] and (int(peticion_Actual[1])-int(hora_Ultima_Peticion[1])) < 2:
        return True
    else:
        return False
    
def mandar_mensajes_Admin(request,mensaje):
    datos = models.administradores.objects.get(nombreUsuario=request.session['usuario'])
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(datos.tokenTelegram)
    subprocess.call('curl -s --max-time 5 -d "chat_id={0}&disable_web_page_preview=1&text={1}" {2} >/dev/null'.format(datos.telegram,mensaje,url),shell=True)
    
def validacion_cadena(cadena):
    expresion_regular = r'^[a-zA-Z0-9äöüÄÖÜ]*$'
    if re.match(expresion_regular,cadena):
        return True
    else:
        return False
    
def validar_ip(ip):
   ip = ip.split('.')
   if len(ip) == 4:
      for octeto in ip:
         if len(octeto) <= 3 and octeto.isdigit() and int(octeto) <= 255:
            pass
         else:
            return False
   else:
      return False
   return True

def registrar_Adminstradores(nombreAdmin,nombreUsuario,password,ip_servidor,tokenTelegram,id_chat_telegram):
    #registro = models.administradores()
    print(nombreAdmin,nombreUsuario,password,ip_servidor,tokenTelegram,id_chat_telegram)
    pass
    
def validar_password(password):
    if len(password) >= 10:
        if validarNumero(password):
            if validarMinusculas(password):
                if validarMayusculas(password):
                    if validar_Caracter_Especial(password):
                        return True
    else:
        return False

def validarNumero(password):
    for numero in password:
        if numero.isdigit():
            return True

def validarMayusculas(password):
    for mayusculas in password:
        if mayusculas.isupper():
            return True
        
def validarMinusculas(password):
    for minusculas in password:
        if minusculas.islower():
            return True
        
def validar_Caracter_Especial(password):
    caracteres_especiales = '!@#$%^&*()[]{};:,./<>?\|`~-=_+'
    for caracterEspecial in caracteres_especiales:
        for letra in password:
            if letra == caracterEspecial:
                print("bien")
                return True
            
def cifrar(mensaje, llave_aes, iv):
    aesCipher = Cipher(algorithms.AES(llave_aes), modes.CTR(iv),
                       backend=default_backend())
    cifrador = aesCipher.encryptor()    
    cifrado = cifrador.update(mensaje)
    cifrador.finalize()
    return cifrado

def descifrar(cifrado, llave_aes, iv):
    aesCipher = Cipher(algorithms.AES(llave_aes), modes.CTR(iv),
                       backend=default_backend())
    descifrador = aesCipher.decryptor()
    plano = descifrador.update(cifrado)
    descifrador.finalize()
    return plano

def generar_llave():
    llave_aes = os.urandom(16)
    iv = os.urandom(16)
    return llave_aes, iv

def cifrar_credenciales(usuario,password,llave_aes_usr, iv_usr, llave_aes_pwd, iv_pwd):
    usuario_cifrado = cifrar(usuario.encode('utf-8'), llave_aes_usr, iv_usr)
    password_cifrado = cifrar(password.encode('utf-8'), llave_aes_pwd, iv_pwd)
    return usuario_cifrado, password_cifrado
    
def convertir_dato_base64(dato):
    return base64.b64encode(dato).decode('utf-8')

def clear_cache(request):
    """Clears the complete cache. """
    # memcached
    try:
        cache._cache.flush_all()
    except AttributeError:
        pass
    
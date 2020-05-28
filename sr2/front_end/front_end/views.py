#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:00:21 2020

@author: josrall
"""
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from front_end import decoradores
from monitor import models
import front_end.back_end as back_end
## aqui tienes que checar lo del cambio de nombre de funciones de la clase 12 de mayo
LOGIN = '/login/'
@csrf_exempt
def login(request):
    t = 'login.html'
    if request.method == 'GET':
        return render(request, t, {'ban': True})
    elif request.method == 'POST':
        if back_end.dejar_pasar_peticion_login(request):
            usuario = request.POST.get('usuario').strip()
            password = request.POST.get('pass').strip()
            if back_end.validacion_cadena(str(usuario)) and back_end.validar_password(str(password)):  
                try:
                    models.administradores.objects.get(nombreUsuario=usuario, password=password)
                    request.session['usuario'] = usuario
                    request.session['password'] = password
                    request.session['codigo'] = back_end.obtener_Codigo(request)
                    request.session['logueado'] = True
                    return redirect("/inicio/")
                except:
                    return render(request, t, {'errores': 'Usuario/contraseña son incorrectos','ban':True})
            else:
                return render(request, t, {'errores': 'Usuario/contraseña son incorrectos','ban':True})
        else:
            return render(request,t, {'errores': 'Demasiados intentos fallidos','ban':False})
            
            
## intenta dejar en la misma vista inicio y comprobar
@decoradores.esta_logueado
def inicio(request):
    user_s = request.session['usuario']
    t = 'comprobar.html'
    if request.method == 'GET' and request.session['logueado']:
        back_end.mandar_codigo(request)
        return render(request, t,)
    elif request.method == 'POST':
        if back_end.validar_token(request):
            codigo_Recuperado = request.POST.get('codigo')
            if codigo_Recuperado == request.session['codigo']:
                llave_aes_usr, iv_usr = back_end.generar_llave()
                llave_aes_pwd, iv_pwd = back_end.generar_llave()
                usuario_cifrado, password_cifrado = back_end.cifrar_credenciales(request.session['usuario'], 
                                                    request.session['password'], llave_aes_usr, iv_usr, 
                                                    llave_aes_pwd, iv_pwd)
                #request.session['usuario'] =  back_end.convertir_dato_base64(usuario_cifrado)
                request.session['password'] = back_end.convertir_dato_base64(password_cifrado)
                t = 'inicio.html'
                request.session['codigo'] = None
                return render(request,t,{'logueado': request.session['logueado'],'user': user_s,
                            'llave_aes_usr': back_end.convertir_dato_base64(llave_aes_usr),
                            'iv_usr': back_end.convertir_dato_base64(iv_usr),
                            'llave_aes_pwd': back_end.convertir_dato_base64(llave_aes_usr), 
                            'iv_pwd': back_end.convertir_dato_base64(iv_pwd)})
            else:
                request.session.flush()
                return redirect(LOGIN)
        else:
            request.session.flush()
            return redirect(LOGIN)
    
def registrar_administrador(request):
    t = 'registro.html'
    if request.session['usuario'] != 'adminGlobal':
        return redirect('/inicio/')
    else:
        if request.method == 'GET':
            return render(request,t,{'logueado':request.session['logueado'],'usuario_logueado':request.session['usuario']})
        elif request.method == 'POST':
            nombreAdmin = request.POST.get('nombreAdmin')
            nombreUsuario = request.POST.get('nombreUsuario')
            password = request.POST.get('pass')
            ip_servidor = request.POST.get('ip_servidor')
            tokenTelegram = request.POST.get('token_telegram')
            id_chat_telegram = request.POST.get('id_chat')
            if not back_end.validar_ip(ip_servidor):
                return render(request,t,{'logueado':request.session['logueado'],
                                         'usuario_logueado':request.session['usuario'],
                                         'errores':'La ip es incorrecta'})
            if not back_end.validar_password(password):
                return render(request,t,{'logueado':request.session['logueado'],
                                         'usuario_logueado':request.session['usuario'],
                                         'errores':'El password debe tener mínimo 10 carácteres, mayúsculas, minúsuclas, dígitos, un carácter especial'})
            back_end.registrar_Adminstradores(nombreAdmin,nombreUsuario,password,ip_servidor,tokenTelegram,id_chat_telegram)
            return render(request,t,{'logueado':request.session['logueado'],
                                         'usuario_logueado':request.session['usuario'],
                                         'errores':'bien'})
        
def logout(request):
    request.session.flush()
    return redirect(LOGIN)
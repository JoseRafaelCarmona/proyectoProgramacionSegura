from rest_framework import viewsets
from .serializers import ServidorSerializer
from django.http import HttpResponse
import json, request, logging
from .back_end import *
# Create your views here.

class ServidorViewSet(viewsets.ModelViewSet):
    serializer_class = ServidorSerializer
    queryset = servidor.objects.all()

    def __init__(self, *args, **kwargs):
        registrar_datos_servidor()

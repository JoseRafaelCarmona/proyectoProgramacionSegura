from rest_framework import serializers
from .models import servidor

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = servidor
        fields = ('memoria_ram','memoria_swap','espacio_disco','numero_procesadores')

from rest_framework import serializers
from .models import Unidades, Clientes, Contrato, Pago
class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidades
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

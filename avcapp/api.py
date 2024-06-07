from rest_framework import viewsets, permissions
from .models import Unidades, Clientes, Contrato, Pago
from .serializers import UnidadesSerializer, ClientesSerializer, PagoSerializer, ContratoSerializer
from rest_framework.response import Response
from rest_framework import status

class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadesSerializer
    

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientesSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ContratoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer

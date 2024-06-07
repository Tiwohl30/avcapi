from django.db import models
from django.utils import timezone

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, null=True)
    correo_electronico = models.EmailField(unique=True, null=True)
    numero_identificacion = models.CharField(max_length=50, unique=True,null=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Unidades(models.Model):


    num_unidad = models.AutoField(primary_key=True)
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('EN_ARRIENDO', 'En Arriendo'),
        ('MANTENIMIENTO', 'Mantenimiento'),
    ]
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField(null=True)
    numero_de_serie = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=20)
    placa = models.CharField(max_length=20, unique=True)
    kilometraje = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
    


class Contrato(models.Model):
    ESTADOS_CONTRATO = [
        ('ACTIVO', 'Activo'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    unidad = models.ForeignKey('Unidades', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_contrato = models.CharField(max_length=25, choices=ESTADOS_CONTRATO, default='ACTIVO')

    def __str__(self):
        return f"Contrato {self.id} - {self.cliente} - {self.unidad}"

    def calcular_precio_total(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        self.precio_total = dias * self.unidad.precio_alquiler_por_dia
        return self.precio_total
    
    def save(self, *args, **kwargs):
        if self.estado_contrato == 'ACTIVO' and self.fecha_fin < timezone.now().date():
            self.estado_contrato = 'FINALIZADO'
        super().save(*args, **kwargs)

    class Meta:
        permissions = [
            ("can_finalize_contract", "Puede finalizar contratos"),
        ]



class Pago(models.Model):
    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA_CREDITO', 'Tarjeta de Crédito'),
        ('TRANSFERENCIA_BANCARIA', 'Transferencia Bancaria'),
    ]

    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    fecha_pago = models.DateField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=80, choices=METODOS_PAGO)

    def __str__(self):
        return f"Pago {self.id} - {self.contrato} - {self.monto_pagado}"
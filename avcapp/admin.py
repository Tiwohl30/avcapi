from django.contrib import admin
from .models import Clientes, Unidades, Pago, Contrato



# Register your models here.
admin.site.register(Clientes)
admin.site.register(Unidades)
admin.site.register(Pago)
admin.site.register(Contrato)
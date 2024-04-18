

def calcular_cotizacion(valor_auto, cuotas):
    porcentaje_entrega = 0.6
    entrega_inicial = valor_auto * porcentaje_entrega
    monto_cuota = valor_auto * (1 - porcentaje_entrega) / cuotas
    return entrega_inicial, monto_cuota

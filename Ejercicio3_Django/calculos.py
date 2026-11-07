# EJERCICIO 3 - ECOTECH SOLUTIONS

# Calcular las emisiones de carbono
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):

    # Verificar que el consumo no sea negativo
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    # Calcular las emisiones
    emisiones = consumo_kwh * factor_emision

    return emisiones
# Obtener las metricas de consumo de las plantas
def obtener_metricas_consumo(registros):

    total_emisiones = 0
    consumo_por_planta = {}

    # Recorrer los registros de consumo
    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        # Calcular las emisiones usando la funcion anterior
        emisiones = calcular_emisiones_carbono(consumo)

        total_emisiones += emisiones

        # Acumular el consumo de cada planta
        if planta in consumo_por_planta:
            consumo_por_planta[planta] += consumo
        else:
            consumo_por_planta[planta] = consumo

    # Identificar la planta con mayor consumo
    if consumo_por_planta:
        planta_mayor_consumo = max(
            consumo_por_planta,
            key=consumo_por_planta.get
        )
    else:
        planta_mayor_consumo = "Sin registros"

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo
    }

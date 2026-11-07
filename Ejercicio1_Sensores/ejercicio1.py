def limpiar_registro_sensor(registro_raw):
    """
    Limpia y normaliza los datos recibidos de un sensor.
    """

    # Limpiar el identificador del sensor
    sensor_id = registro_raw.get("sensor_id", "").strip()

    # Convertir la temperatura a un número decimal
    temperatura_texto = str(registro_raw["temperatura"])
    temperatura_limpia = temperatura_texto.strip().replace("C", "").replace("c", "").replace("°", "")
    temperatura = float(temperatura_limpia)

    # Asignar una ubicación segura si no existe
    ubicacion = registro_raw.get("ubicacion") or "Ubicación no registrada"
    ubicacion = ubicacion.strip()

    # Crear un nuevo diccionario con los datos limpios
    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio

# Prueba del Punto A
registro_prueba = {
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": "Planta Norte"
}

resultado = limpiar_registro_sensor(registro_prueba)

print("RESULTADO DEL SENSOR LIMPIO:")
print(resultado)

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Genera un resumen estadístico de los sensores.
    """

    lista_sensores_alerta = []
    suma_temperaturas = 0

    # Recorrer todos los sensores
    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]

        # Detectar temperaturas superiores al límite
        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

        # Acumular las temperaturas
        suma_temperaturas += temperatura

    # Calcular el promedio
    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0.0

    return lista_sensores_alerta, promedio_temperatura

# EJECUCION COMPLETA DEL SISTEMA ECOTECH

registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": " SENSOR-002 ", "temperatura": "38C", "ubicacion": "Planta Sur"},
    {"sensor_id": " SENSOR-003 ", "temperatura": "42.5C", "ubicacion": "Planta Este"},
    {"sensor_id": " SENSOR-004 ", "temperatura": "21C", "ubicacion": ""}
]

# Limpiar todos los registros
sensores_limpios = []

for registro in registros_crudos:
    sensor_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(sensor_limpio)

# Establecer el limite de temperatura
umbral = 35.0

# Generar el resumen
alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)

# Mostrar el reporte final
print("\n========== REPORTE ECOTECH SOLUTIONS ==========")

print("\nSensores procesados:", len(sensores_limpios))

print("\nSensores con temperatura elevada:")
for sensor_id in alertas:
    print("-", sensor_id)

print("\nPromedio de temperatura:", round(promedio, 2), "°C")

print("\n===============================================")
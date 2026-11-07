from django.shortcuts import render
from calculos import obtener_metricas_consumo


def inicio(request):
    return render(request, 'sustentabilidad/inicio.html')


def metricas(request):
    registros = [
        {"planta": "Planta Solar", "consumo_kwh": 100},
        {"planta": "Planta Eólica", "consumo_kwh": 150},
        {"planta": "Planta Solar", "consumo_kwh": 50}
    ]

    resultado = obtener_metricas_consumo(registros)

    return render(request, 'sustentabilidad/inicio.html', resultado)
def vista_panel_sustentabilidad(request):

    registros = [
        {"planta": "Planta Solar", "consumo_kwh": 100},
        {"planta": "Planta Eólica", "consumo_kwh": 150},
        {"planta": "Planta Solar", "consumo_kwh": 50}
    ]

    resultado = obtener_metricas_consumo(registros)

    return render(
        request,
        'sustentabilidad/panel.html',
        resultado
    )

# Create your views here.

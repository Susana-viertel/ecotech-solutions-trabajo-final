EcoTech Solutions – Trabajo Práctico Final

Descripción del proyecto

Este proyecto integra tres ejercicios de programación en Python para EcoTech Solutions. Se trabajan la limpieza y el análisis de datos, la programación orientada a objetos, el manejo de excepciones, la persistencia de información, las pruebas unitarias y el desarrollo web con Django.

Estructura del proyecto

Ejercicio 1 – Sensores

Limpieza y normalización de registros de sensores.

Conversión de temperaturas a valores numéricos.

Detección de temperaturas superiores al umbral.

Cálculo del promedio de temperatura.

Generación de un reporte final.

Archivo principal: Ejercicio1_Sensores/ejercicio1.py

Ejercicio 2 – Inventario

Clase DispositivoEcológico.

Excepción personalizada StockInvalidoError.

Encapsulamiento y validación del stock.

Herencia y polimorfismo mediante PanelSolar.

Exportación del catálogo a formato JSON.

Archivos principales:

Ejercicio2_Inventario/ejercicio2.py

Ejercicio2_Inventario/catalogo_ecotech.json

Ejercicio 3 – Auditoría e integración Django

Cálculo de emisiones de carbono.

Pruebas unitarias con unittest.

Procesamiento de métricas de consumo.

Aplicación web desarrollada con Django.

Panel de sustentabilidad con plantilla HTML y estilos CSS.

Proyecto Django: Ejercicio3_Django/

Tecnologías utilizadas

Python

Django

unittest

JSON

HTML

CSS

Ejecución

Cada ejercicio Python puede ejecutarse desde la carpeta principal utilizando los comandos:

python Ejercicio1_Sensores/ejercicio1.py
python Ejercicio2_Inventario/ejercicio2.py

Para ejecutar las pruebas del Ejercicio 3, ingresar en la carpeta Ejercicio3_Django y ejecutar:

python -m unittest test_calculos

Para iniciar el servidor Django, ingresar en Ejercicio3_Django y ejecutar:

python manage.py runserver

Luego abrir en el navegador:

http://127.0.0.1:8000/sustentabilidad/panel/

Proyecto académico

EcoTech Solutions – Trabajo Práctico Final.
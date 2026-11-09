# EJERCICIO 2 - ECOTECH SOLUTIONS

# Excepcion personalizada para controlar el stock
import json
from pathlib import Path
class StockInvalidoError(Exception):
    """Error que se produce cuando el stock es negativo."""
    pass
# Clase base de los productos ecologicos
class DispositivoEcológico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Propiedad para consultar el stock
    @property
    def stock(self):
        return self._stock

    # Controlar el stock mediante encapsulamiento
    @stock.setter
    def stock(self, cantidad):
        if cantidad < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self._stock = cantidad

    # Ficha tecnica comercial del producto
    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock disponible: {self.stock}"
        )

    # Clase hija: Panel Solar
class PanelSolar(DispositivoEcológico):

    def __init__(self, nombre, precio, stock, potencia, eficiencia):
        # Heredar los atributos de la clase padre
        super().__init__(nombre, precio, stock)

        # Atributos propios del panel solar
        self.potencia = potencia
        self.eficiencia = eficiencia

    # Polimorfismo: personalizar la ficha tecnica
    def ficha_tecnica(self):
        return (
            f"=== FICHA TECNICA DEL PANEL SOLAR ===\n"
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock disponible: {self.stock}\n"
            f"Potencia: {self.potencia} W\n"
            f"Eficiencia: {self.eficiencia}%"
        )
    # Clase encargada de guardar el catalogo
class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):

        catalogo = []

        # Recorrer los productos del inventario
        for dispositivo in lista_dispositivos:

            producto = {
                "tipo": dispositivo.__class__.__name__,
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.stock
            }

            # Agregar datos especificos de PanelSolar
            if isinstance(dispositivo, PanelSolar):
                producto["potencia"] = dispositivo.potencia
                producto["eficiencia"] = dispositivo.eficiencia

            catalogo.append(producto)

        # Guardar los productos en formato JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)
            # ==========================================
# PRUEBAS DEL SISTEMA ECOTECH SOLUTIONS
# ==========================================

# Crear productos validos
producto1 = DispositivoEcológico(
    "Lampara LED Ecologica", 15000, 20
)

producto2 = PanelSolar(
    "Panel Solar EcoTech", 250000, 10, 450, 22.5
)

# Probar la excepcion de stock negativo
print("\n--- PRUEBA DE STOCK INVALIDO ---")

try:
    producto1.stock = -5

except StockInvalidoError as error:
    print("Error controlado:", error)

# Mostrar las fichas tecnicas
print("\n--- CATALOGO DE PRODUCTOS ---")

print(producto1.ficha_tecnica())
print()
print(producto2.ficha_tecnica())

# Crear la lista de productos validos
productos = [producto1, producto2]

# Exportar el catalogo a JSON
GestorInventario.guardar_catalogo_json(
    productos,
  Path(__file__).resolve().parent / "catalogo_ecotech.json"
)

print("\n--- PROCESO FINALIZADO ---")

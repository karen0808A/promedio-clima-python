# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        # Encapsulamiento de la lista de temperaturas
        self.__temperaturas = []

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Función principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal del clima es: {promedio:.2f} °C")

# Ejecución del programa
main()

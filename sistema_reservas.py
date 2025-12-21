# Sistema de Reservas de Hotel
# Ejemplo del mundo real usando Programación Orientada a Objetos

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion
        self.habitacion.reservar()

    def mostrar_detalle(self):
        print("=== Detalle de la Reserva ===")
        print("Cliente:", self.cliente.nombre)
        print("Habitación:", self.habitacion.numero)
        print("Tipo:", self.habitacion.tipo)
        print("Precio:", self.habitacion.precio)


# Programa principal
habitacion1 = Habitacion(101, "Simple", 30)
cliente1 = Cliente("Karen Silvana", "0102030405")

reserva1 = Reserva(cliente1, habitacion1)
reserva1.mostrar_detalle()

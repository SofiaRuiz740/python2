# reserva.py

from cliente import Cliente  # Importamos la clase Cliente

class Reserva:
    def __init__(self):
        self._numero_habitacion = 0
        self._cantidad_noches = 0
        self._cliente = None

    def get_numero_habitacion(self):
        return self._numero_habitacion

    def set_numero_habitacion(self, numero):
        self._numero_habitacion = numero

    def get_cantidad_noches(self):
        return self._cantidad_noches

    def set_cantidad_noches(self, noches):
        self._cantidad_noches = noches

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

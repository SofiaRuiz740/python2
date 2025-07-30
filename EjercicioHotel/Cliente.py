# cliente.py

class Cliente:
    def __init__(self):
        self._nombre = ""
        self._telefono = ""

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

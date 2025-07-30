# cuenta_bancaria.py

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial):
        self._titular = titular
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo_inicial

    # Métodos GET (sin método SET directo al saldo)
    def get_titular(self):
        return self._titular

    def get_numero_cuenta(self):
        return self._numero_cuenta

    def get_saldo(self):
        return self._saldo

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            return True
        return False

    # Método para retirar dinero
    def retirar(self, monto):
        if monto > 0 and self._saldo >= monto:
            self._saldo -= monto
            return True
        return False

    # Método para transferir dinero a otra cuenta
    def transferir(self, cuenta_destino, monto):
        if self.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False

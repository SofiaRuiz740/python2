# main.py

from cliente import Cliente
from reserva import Reserva

def main():
    print("----- REGISTRO DE RESERVA DE HOTEL -----\n")

    # Crear objeto Cliente
    cliente = Cliente()
    cliente.set_nombre(input("Ingrese el nombre del cliente: "))
    cliente.set_telefono(input("Ingrese el teléfono del cliente: "))

    # Crear objeto Reserva
    reserva = Reserva()
    reserva.set_numero_habitacion(int(input("Ingrese el número de habitación: ")))
    reserva.set_cantidad_noches(int(input("Ingrese la cantidad de noches: ")))

    # Asociar cliente a la reserva
    reserva.set_cliente(cliente)

    # Mostrar resumen
    resumen = f"""
    --------- RESUMEN DE LA RESERVA ---------
    Nombre del cliente: {reserva.get_cliente().get_nombre()}
    Teléfono: {reserva.get_cliente().get_telefono()}
    Número de habitación: {reserva.get_numero_habitacion()}
    Cantidad de noches: {reserva.get_cantidad_noches()}
    ------------------------------------------
    """
    print(resumen)

if __name__ == "__main__":
    main()

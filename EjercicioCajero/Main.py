# main.py

from cuenta_bancaria import CuentaBancaria

def main():
    print("===== SIMULADOR DE CAJERO AUTOMÁTICO =====\n")

    # Inicialización: crear dos cuentas
    cuenta_principal = CuentaBancaria("Juan Pérez", "123-456", 2_000_000)
    cuenta_destino = CuentaBancaria("Ana Gómez", "987-654", 500_000)

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Consultar Saldo")
        print("2. Realizar un Depósito")
        print("3. Realizar un Retiro")
        print("4. Realizar una Transferencia")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            print(f"\nSaldo actual: ${cuenta_principal.get_saldo():,.2f}")

        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                if cuenta_principal.depositar(monto):
                    print(f"Depósito exitoso. Nuevo saldo: ${cuenta_principal.get_saldo():,.2f}")
                else:
                    print("Monto inválido. Intente de nuevo.")
            except ValueError:
                print("Error: debe ingresar un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                if cuenta_principal.retirar(monto):
                    print(f"Retiro exitoso. Nuevo saldo: ${cuenta_principal.get_saldo():,.2f}")
                else:
                    print("Saldo insuficiente o monto inválido.")
            except ValueError:
                print("Error: debe ingresar un número válido.")

        elif opcion == "4":
            try:
                monto = float(input("Ingrese el monto a transferir: "))
                if cuenta_principal.transferir(cuenta_destino, monto):
                    print(f"Transferencia exitosa a {cuenta_destino.get_titular()}.\n"
                          f"Nuevo saldo: ${cuenta_principal.get_saldo():,.2f}")
                else:
                    print("Transferencia fallida. Verifique el saldo o el monto.")
            except ValueError:
                print("Error: debe ingresar un número válido.")

        elif opcion == "5":
            print("\nGracias por usar el cajero automático. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

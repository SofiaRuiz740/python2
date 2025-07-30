from Partido import Partido
from Comprador import Comprador

def crear_partido():
    return Partido("Deportes Quindío", "América de Cali", "Domingo, 28 de Julio, 2025")

def mostrar_menu(partido):
    print("\n--- Taquilla Virtual ---")
    print(f"Partido: {partido.equipo_local} vs {partido.equipo_visitante}")
    print(f"Fecha: {partido.fecha}")
    print("1. Comprar Boleta")
    print("2. Consultar Disponibilidad")
    print("3. Ver Dinero Recaudado")
    print("4. Salir")

def comprar_boleta(boletas_disponibles, precios, dinero_recaudado):
    nombre = input("Nombre del comprador: ")
    documento = input("Documento del comprador: ")
    comprador = Comprador(nombre, documento)

    localidades = list(boletas_disponibles.keys())
    print("\nSeleccione la localidad:")
    for i, loc in enumerate(localidades, 1):
        print(f"{i}. {loc} (Precio: ${precios[loc]}, Disponibles: {boletas_disponibles[loc]})")

    opcion = input("Número de localidad: ")
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(localidades):
        print("Localidad inválida.")
        return dinero_recaudado

    localidad = localidades[int(opcion) - 1]

    cantidad = input("Cantidad de boletas a comprar: ")
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Cantidad inválida.")
        return dinero_recaudado

    cantidad = int(cantidad)

    if cantidad > boletas_disponibles[localidad]:
        print(f"No hay suficientes boletas en la localidad {localidad}.")
        return dinero_recaudado

    costo_total = precios[localidad] * cantidad
    boletas_disponibles[localidad] -= cantidad
    dinero_recaudado += costo_total

    print("\n--- Recibo de Compra ---")
    print(f"Comprador: {comprador.nombre} - Documento: {comprador.documento}")
    print(f"Localidad: {localidad}")
    print(f"Cantidad: {cantidad}")
    print(f"Total pagado: ${costo_total}")
    print("------------------------")

    return dinero_recaudado

def consultar_disponibilidad(boletas_disponibles):
    print("\n--- Disponibilidad de Boletas ---")
    total = sum(boletas_disponibles.values())
    for loc, disp in boletas_disponibles.items():
        print(f"{loc}: {disp} boletas disponibles")
    print(f"Total general: {total} boletas disponibles\n")

def ver_dinero_recaudado(dinero_recaudado):
    print(f"\nDinero recaudado hasta el momento: ${dinero_recaudado}\n")

def main():
    partido = crear_partido()

    boletas_disponibles = {
        "Norte": 100,
        "Sur": 100,
        "VIP": 20
    }
    precios = {
        "Norte": 50000,
        "Sur": 50000,
        "VIP": 200000
    }
    dinero_recaudado = 0

    while True:
        mostrar_menu(partido)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dinero_recaudado = comprar_boleta(boletas_disponibles, precios, dinero_recaudado)
        elif opcion == "2":
            consultar_disponibilidad(boletas_disponibles)
        elif opcion == "3":
            ver_dinero_recaudado(dinero_recaudado)
        elif opcion == "4":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

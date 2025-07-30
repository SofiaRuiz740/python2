from Monitor import Monitor

#lista de objetos
def crear_monitores():
    return [
        Monitor("Maithe Mejia", "101", "Feria Universitaria - Unicentro"),
        Monitor("Carlos Rojas", "102", "Visita Colegio San Luis Rey"),
        Monitor("Sofia Ruiz", "103", "Charla Vocacional - ITI"),
        Monitor("David Silva", "104", "Feria Educativa - El Edén"),
        Monitor("Arle Morales", "105", "Taller de Orientación - Colegio Bolívar")
    ]

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar Horas de un Monitor")
    print("2. Ver Estado de Todos los Monitores")
    print("3. Salir")

def registrar_horas(monitores):
    print("Seleccione el monitor:")
    for i, monitor in enumerate(monitores, 1):
        print(f"{i}. {monitor.nombre}")

    opcion = int(input("Número del monitor: "))
    if 1 <= opcion <= len(monitores):
        horas = float(input("Ingrese las horas a registrar: "))
        monitores[opcion - 1].registrar_horas(horas)
        print(f"Horas registradas para {monitores[opcion - 1].nombre}. Total acumulado: {monitores[opcion - 1].horas_acumuladas} horas.\n")
    else:
        print("Opción inválida.\n")

def ver_estado_todos(monitores):
    print("\n--- Estado de todos los monitores ---")
    for monitor in monitores:
        print(f"Nombre: {monitor.nombre}")
        print(f"Código: {monitor.codigo_estudiante}")
        print(f"Evento: {monitor.evento_asignado}")
        print(f"Horas acumuladas: {monitor.horas_acumuladas}")
        print(f"Estado: {monitor.verificar_estado()}")
        print("-" * 40)
    print()

def main():
    monitores = crear_monitores()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_horas(monitores)
        elif opcion == "2":
            ver_estado_todos(monitores)
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()

def mostrar_menu():
    print("---- MENU ----")
    print("1. Agregar contacto")
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    print()

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")

    with open("archivo.txt", "a") as archivo:
        archivo.write(f"{nombre},{numero}\n")
    print("Contacto agregado exitosamente.")
    print()
def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    nuevo_numero = input("Ingrese el nuevo número de teléfono: ")
    lineas_actualizadas = []
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0] == nombre:
                linea = f"{nombre},{nuevo_numero}\n"
            lineas_actualizadas.append(linea)
    with open("archivo.txt", "w") as archivo:
        archivo.writelines(lineas_actualizadas);
    if any(lineas_actualizadas):
        print("Contacto actualizado exitosamente.");
    else:
        print("No se encontró el contacto en la agenda.")
    print()
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    lineas_actualizadas = []
    with open("agenda.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0] != nombre:
                lineas_actualizadas.append(linea)

    with open("agenda.txt", "w") as archivo:
        archivo.writelines(lineas_actualizadas)

    if any(lineas_actualizadas):
        print("Contacto eliminado exitosamente.")
    else:
        print("No se encontró el contacto en la agenda.")
    print()
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            actualizar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        print()
main()

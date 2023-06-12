#def agregar_contacto():
   # nombre = input("Ingrese el nombre del contacto: ")
    #numero = input("Ingrese el número de teléfono: ")

    #with open("archivo.txt", "a") as archivo:
       # archivo.write(nombre + "," + numero + "\n")

# Ejemplo de uso
#agregar_contacto()
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

    with open("agenda.txt", "a") as archivo:
        archivo.write(nombre + "," + numero + "\n")
    
    print("Contacto agregado exitosamente.")
    print()

def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    nuevo_numero = input("Ingrese el nuevo número de teléfono: ")

    with open("archivo.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False

    with open("archivo.txt", "w") as archivo:
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] == nombre:
                archivo.write(nombre + "," + nuevo_numero + "\n")
                encontrado = True
            else:
                archivo.write(linea)

    if encontrado:
        print("Contacto actualizado exitosamente.")
    else:
        print("No se encontró el contacto en la agenda.")
    print()

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")

    with open("archivo.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False

    with open("archivo.txt", "w") as archivo:
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] != nombre:
                archivo.write(linea)
            else:
                encontrado = True

    if encontrado:
        print("Contacto eliminado exitosamente.")
    else:
        print("No se encontró el contacto en la agenda.")
    print()

# Función principal del programa
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

# Ejecutar el programa
main();
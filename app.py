personas = []
iteracion = True

while iteracion:
    peticion = input("Por favor ingrese qué tipo de acción quiere realizar:\n"
                     "1. Ingresar nueva persona\n"
                     "2. Mostrar todos los datos\n"
                     "3. Filtrar por DNI\n"
                     "4. Salir del programa\n"
                     ": ")

    if peticion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        dni = input("Ingrese el DNI de la persona: ")

        telefonos = []
        iteracion2 = True

        while iteracion2:
            telefono = input("Ingrese los teléfonos de la persona: ")
            telefonos.append(telefono)
            continuar = input("Desea ingresar otro teléfono? (s/n): ")
            if continuar == "n":
                iteracion2 = False

        hijos = input("Ingrese los hijos de la persona separados por coma: ").split(",")

        personas.append([nombre, apellido, dni, telefonos, hijos])
        print(personas)

    elif peticion == "2":
        print("Lista de personas:")
        print(personas)

    elif peticion == "3":
        dni_buscado = input("Ingrese el DNI de la persona que desea buscar: ")
        persona_encontrada = next((persona for persona in personas if persona[2] == dni_buscado), None)

        if persona_encontrada:
            print("Persona encontrada:", persona_encontrada)
        else:
            print("No se encontró ninguna persona con ese DNI.")

    elif peticion == "4":
        iteracion = False
        print("Saliendo del programa...")

    else:
        print("Opción no válida.")

print(personas)

salir = False
while salir == False:
    print("1. Saludar\n2. Despedirse\n3. Salir")
    seleccion = input("selecciona una opcion: ")
    match seleccion:
        case "1":
            print("Hola")
        case "2":
            print("Hasta pronto...")
        case "3":
            print("Saliendo...")
            salir = True
        case _:
            print("opcion no valida")


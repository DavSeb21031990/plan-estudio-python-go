print("Programa para ingresar números")
print("------------------------------------------------")
value = input("Ingrese un número entero (o 'salir' para terminar): ")
while value != "salir":
    try:
        num = int(value)
        print(f"El número ingresado es: {num}")
    except ValueError:
        print("Error: No se pudo convertir el valor ingresado a un número",
              " entero.")
        break
    value = input("Ingrese otro número entero (o 'salir' para terminar): ")
print("Programa finalizado.")

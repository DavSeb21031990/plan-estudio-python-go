import Wednesday.Exercise_1.utils as utils

print("Inicio Programa")
print("------------------------------------------------------", end="\n")
print("Selecione una opción: ")
print("1. Verificar si un número es par o impar")
print("2. Convertir Celsius a Fahrenheit")
print("3. Salir")
print()

opcion = input("Ingrese su opción: ")
while opcion != "3":
    if opcion == "1":
        utils.es_par_o_impar()
    elif opcion == "2":
        utils.convertir_celsius_a_fahrenheit()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
    print()
    print("------------------------------------------------------", end="\n")
    print("Selecione una opción: ")
    opcion = input("Ingrese su opción: ")

print("Saliendo del programa...")

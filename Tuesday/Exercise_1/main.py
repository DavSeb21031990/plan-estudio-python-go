print("Programa para verificar si un número es par o impar")
try:
    numero = input("Ingrese un número entero: ")
    if int(numero) % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
print("Fin del programa")

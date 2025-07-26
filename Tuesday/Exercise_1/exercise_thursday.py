def validate_is_pair(numero):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def get_number():
    try:
        numero = input("Ingrese un número entero: ")
        return int(numero)
    except TypeError:
        return 0
        print("Error: Debe ingresar un número entero válido.")


print("Programa para verificar si un número es par o impar")
validate_is_pair(get_number())
print("Fin del programa")

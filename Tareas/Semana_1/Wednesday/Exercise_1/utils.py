def es_par_o_impar():
    print()
    try:
        numero = input("Ingrese un número entero: ")
        if int(numero) % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


def convertir_celsius_a_fahrenheit():
    print()
    celsius = input("Ingrese los grados en Celsius: ")
    fanrenheit = (float(celsius) * (9 / 5)) + 32
    print()
    print(f"Resultado: °{celsius} celsius es igual a °{fanrenheit:.2f}")

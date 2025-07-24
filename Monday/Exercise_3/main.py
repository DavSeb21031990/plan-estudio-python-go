"""
- A = pi * r^2
"""

import math


def header():
    print("------------------------------------------------------")
    print("Calcular área de un círculo")
    print("Inicio Programa")
    print("------------------------------------------------------", end="\n")


def calculateArea():
    PI = math.pi
    radio = input("Ingrese en valor del radio del circulo: ")
    area = PI * (float(radio) ** 2)
    print(f"Resultado: El área del circulo es {area:.2f}")


header()
calculateArea()

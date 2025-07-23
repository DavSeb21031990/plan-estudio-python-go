"""
- A = pi * r^2
"""

import math

print("Calcular área de un circulo")
print("Inicio Programa")
print("------------------------------------------------------", end="\n")

PI = math.pi

radio = input("Ingrese en valor del radio del circulo: ")
area = PI * (float(radio) ** 2)

print(f"Resultado: El área del circulo es {area:.2f}")

"""
- °F = (°C × 9/5) + 32
"""

print("Convertidor de temperatura de Celsius a Fahrenheit")
print("Inicio Programa")
print("------------------------------------------------------", end="\n")

celsius = input("Ingrese los grados en Celsius: ")
fanrenheit = (float(celsius) * (9 / 5)) + 32

print(f"Resultado: °{celsius} celsius es igual a °{fanrenheit:.2f}")

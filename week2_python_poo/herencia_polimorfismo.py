class Animal:
    def __init__(self):
        pass

    def hacer_sonido(self):
        print("El animal hace un sonido genérico")


class Perro(Animal):
    def __init__(self):
        super().__init__()

    def hacer_sonido(self):
        print("El perro ladra")


class Gato(Animal):
    def __init_(self):
        super().__init__()

    def hacer_sonido(self):
        super().hacer_sonido()
        print("el gato hace miau")


animal_1 = Animal()
animal_2 = Animal()
perro_1 = Perro()
gato_1 = Gato()

animales = [animal_1, animal_2, perro_1, gato_1]

for animal in animales:
    animal.hacer_sonido()

"""
Ejemplo de composición.
- Motor y Autor son dos clases diferentes.
- Autor tiene un motor como atributo de tipo Motor.
"""


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def arrancar(self):
        print(f"Iniciando motor con potencia {self.potencia} "
              f"caballos de fuerza")


class Auto:
    def __init__(self, marca, modelo, potencia_motor=1000):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

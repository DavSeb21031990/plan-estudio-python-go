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
        print("el gato hace miau")


animal_1 = Animal()
animal_2 = Animal()
perro_1 = Perro()
gato_1 = Gato()

animales = [animal_1, animal_2, perro_1, gato_1]

for animal in animales:
    animal.hacer_sonido()

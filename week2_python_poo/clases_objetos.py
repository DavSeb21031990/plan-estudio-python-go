class Coche:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_information(self):
        print(f"Coche: {self.brand} {self.model}, Year: {self.year}")


coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Honda", "Civic", 2021)

coche1.show_information()
coche2.show_information()

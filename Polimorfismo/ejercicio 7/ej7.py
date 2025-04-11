class Animal:
    def __init__(self, nombre, edad=None, raza=None, color=None, tipo=None):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
        self.tipo = tipo

    def hacer_sonido(self):
        if self.raza is not None:
            return "Guau Guau"  # Perro
        elif self.color is not None:
            return "Miau"  # Gato
        elif self.tipo is not None:
            return "Pío Pío"  # Pájaro
        else:
            return "Sonido desconocido"

    def moverse(self):
        if self.raza is not None:
            return "Corre"  # Perro
        elif self.color is not None:
            return "Salta"  # Gato
        elif self.tipo is not None:
            return "Vuela"  # Pájaro
        else:
            return "Movimiento desconocido"

    def mostrar(self):
        print(f"{self.nombre} ({self.__class__.__name__}): {self.hacer_sonido()}, {self.moverse()}")

perro = Animal("Tota", edad=6, raza="Pastor Alemán")
gato = Animal("Tommy", color="Blanco")
pajaro = Animal("Edgard", tipo="Cuervo")

animales = [perro, gato, pajaro]

for animal in animales:
    animal.mostrar()
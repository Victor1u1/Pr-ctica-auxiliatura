class Bloque:
    def __init__(self, tipo, capacidad=None, resistencia=None, daño=None, color=None, capacidad_comida=None):
        self.tipo = tipo
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.daño = daño
        self.color = color
        self.capacidad_comida = capacidad_comida

    def accion(self):
        if self.capacidad is not None:
            return "Almacena objetos"  # BloqueCofre
        elif self.daño is not None:
            return "Explota al activarse"  # BloqueTnt
        elif self.capacidad_comida is not None:
            return "Cocina alimentos"  # BloqueHorno
        else:
            return "Acción desconocida"

    def colocar(self, orientacion="suelo"):
        return f"Bloque {self.tipo} colocado en {orientacion}"

    def romper(self):
        if self.capacidad is not None:
            return "Se rompe y suelta los objetos almacenados"  # BloqueCofre
        elif self.daño is not None:
            return "Explota causando daño"  # BloqueTnt
        elif self.capacidad_comida is not None:
            return "Se rompe y deja caer algo de carbón"  # BloqueHorno
        else:
            return "No pasa nada"

    def mostrar(self):
        print(f"{self.tipo}: {self.accion()} | {self.romper()}")

cofre1 = Bloque("Cofre Grande", capacidad=64, resistencia=10)
cofre2 = Bloque("Cofre Pequeño", capacidad=32, resistencia=8)

tnt1 = Bloque("TNT Normal", daño=20)
tnt2 = Bloque("TNT Potente", daño=40)

horno1 = Bloque("Horno de Piedra", color="Gris", capacidad_comida=10)
horno2 = Bloque("Horno Fundidor", color="Negro", capacidad_comida=20)

bloques = [cofre1, cofre2, tnt1, tnt2, horno1, horno2]

for bloque in bloques:
    bloque.mostrar()

print(cofre1.colocar()) 
print(tnt1.colocar("pared"))  
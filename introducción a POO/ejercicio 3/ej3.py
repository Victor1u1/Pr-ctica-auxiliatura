class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        
    def acelerar(self):
        self.velocidad += 10
    def frenar(self):
        self.velocidad -= 5
        
    def __str__(self):
        return f"{self.marca} {self.modelo} - Velocidad: {self.velocidad}"
        
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ferrari", "296GTB")

coche1.acelerar()
coche1.acelerar()
coche1.frenar()

coche2.acelerar()
coche2.frenar()
coche2.frenar()

print(coche1)
print(coche2)
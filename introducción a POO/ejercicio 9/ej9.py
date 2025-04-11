class Computadora:
    def __init__(self):
        self.componentes = ["CPU", "RAM", "Disco Duro", "Placa base", "Tarjeta gráfica"]
        self.estado = False
    
    def encender(self): self.estado = True
    def apagar(self): self.estado = False
    
    def estado_computadora(self):
        return "Encendido" if self.estado else "Apagada"
        
    def __str__(self):
        return f"Componentes: {','.join(self.componentes)}\nEstado: {self.estado_computadora()}"
        
c = Computadora()
print(c)
c.encender()
print(c)
c.apagar()
print(c)